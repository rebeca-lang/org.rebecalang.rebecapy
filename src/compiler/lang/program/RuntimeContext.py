#!/usr/bin/python
# Filename: RuntimeContext.py
# Description: Implementation of the RuntimeContext class

from collections.abc import Mapping
from compiler.lang.program.Expression import Expression

# Represents an address in the program (function name and instruction pointer)
class Address:
	def __init__(self, fname, ip):
		""" Constructor
		Arguments
			fname -- Function name
			ip -- Instruction pointer
		"""
		self.fname	= fname		# function name
		self.ip 	= ip		# instruction pointer
		return
	
	def __str__(self):
		""" A string notation of the object
		"""
		return f"{self.fname}:{self.ip}"

# Represents the runtime context of the program execution	
class StackFrame:
	def __init__(self, address:Address, return_address:Address, vars=None):
		""" Constructor
		Arguments
			address -- Address of the current instruction
			return_address -- Address to return to after execution
			vars -- Local variables for the stack frame
		"""
		if vars is None:
			vars = {}
		elif isinstance( vars, dict ):
			vars = vars
		elif isinstance( vars, str ):
			vars = dict((k.strip(), v.strip()) for k,v in 
              (item.split('=') for item in vars.split(',')))
		else:
			raise RuntimeError(f'Invalid type for local variables: {type(vars)}')

		self.address	 		= address
		self.return_address 	= return_address
		self.vars 				= vars if vars is not None else {}
		self.thisptr			= None
		return

	def execute(self, runtime, ctxt):
		""" Executes the current instruction
		Arguments
			runtime -- Runtime environment
			ctxt -- Runtime memory context
		"""
		instruction	= ctxt.get(self.address.ip)
		if instruction is None:
			return False
		
		instruction.execute(runtime, ctxt, self)
		return True
	
	def __str__(self):
		""" A string notation of the object
		"""
		return str(self.address)


# Main class managing the runtime context, including the call stack and variable scopes
class RuntimeContext:
	def __init__(self, parent=None):
		""" Constructor
		Arguments
			parent -- Parent runtime context
		"""
		self.stack 			= []
		self.instruction	= None
		self.ax				= None		# accumulator
		self.parent			= parent
		self.log			= []

		self.stack.append(StackFrame(Address("global", 1), None))
		return

	def copy(self, rhs):
		""" Copies the runtime context
		Arguments
			rhs -- Runtime context to copy from
		"""
		# Clone base context
		rhs.instruction	= self.instruction
		rhs.ax			= self.ax
		rhs.parent		= self.parent

		# Clone stack frames
		rhs.stack 		= [ StackFrame(Address(f.address.fname, f.address.ip), f.return_address) 
					 			for f in self.stack ]
		
		# Copy local variables in each stack frame
		for i in range(len(self.stack)):
			rhs.stack[i].vars = self.stack[i].vars.copy()
		
		return rhs
	
	def declare(self, name, value=None):
		""" Declares a new variable in the current scope
		Arguments
			name -- Variable name
			value -- Initial value for the variable
		"""
		assert isinstance( name, str)		
		if self.ip.vars.get(name) is not None:
			raise RuntimeError(f'Variable [{name}] already exists in the current scope.')

		self.ip.vars[name] = value
		return

	def set_self(self, obj):
		""" Sets the 'self' pointer in the current context
		Arguments
			obj -- Object to set as 'self'
		"""
		ip				= self.ip

		# Set the 'self' pointer in the local context
		ip.thisptr 		= obj

		# Set the instance in the map so it 
		# can be accessed by eval()
		ip.vars['self'] = obj
		return
	
	def set(self, name, value):
		""" Sets the value of a variable in the current context
		Arguments
			name -- Variable name
			value -- New value for the variable
		"""
		assert isinstance( name, str)		
		ip 		= self.ip

		if ip.thisptr is not None:
			if name in ip.thisptr.vars:
				ip.thisptr.vars[name]	= value
				return
			
		ip.vars[name] = value
		return

	def test(self):
		""" Tests the runtime context
		"""
		assert isinstance( self.ip.vars, dict)

	def get(self, name):
		""" Retrieves the value of a variable from the current context
		Arguments
			name -- Variable name
		"""
		assert isinstance( name, str)		
		ip 		= self.ip
		if name == 'self':
			return ip.thisptr

		if ip.thisptr is not None:
			value	= ip.thisptr.vars.get(name, None)
			if value is not None:
				return value

		level	= 0

		# Traverse the stack starting with the lowest level
		while True:
			level		= level + 1	
			if level > len(self.stack):
				break

			scope		= self.stack[-level]
			value		= scope.vars.get(name, None)
			if value is not None:
				return value

		return None

	def step(self, ctxt):
		""" Executes the current instruction
		Arguments
			ctxt -- Runtime memory context
		"""
		# Execute the current instruction
		current			= self.stack[-1]
		if current.execute(self, ctxt) == False:
			return False

		# Move the address to the next instruction
		current.address.ip += 1
		return True
	
	@property
	def ip(self):
		""" Returns the instruction pointer for the current stack frame
		"""
		return self.stack[-1]

	@property
	def sp(self):
		""" Returns the stack pointer for the current context
		"""
		return len(self.stack)

	@property
	def numvars(self):
		""" Returns the total number of variables in the current context
		"""
		count = 0
		for f in self.stack:
			count += len(f.vars)
		return count

	@property
	def root(self):
		""" Returns the root runtime context
		"""
		next = self
		while next.parent is not None:
			next = next.parent

		return next

	@property
	def variables(self):
		""" Returns a mapping of variable names to their values in the current context
		"""
		return VariableMapper(self)

	@property
	def callstack(self):
		""" Returns the call stack
		"""
		lines	= []
		level	= 0

		# Traverse the stack starting with the lowest level
		while True:
			level		= level + 1	
			if level > len(self.stack):
				break

			scope		= self.stack[-level]
			lines.append(f"{scope.address.fname}:{scope.address.ip}")

		
		return '\n'.join(lines)

	@property
	def thisptr(self):
		""" Returns the 'this' pointer for the current context
		"""
		return self.ip.thisptr
	
	def next(self):
		""" Advances the instruction pointer to the next instruction
		"""
		self.stack[-1].address.ip += 1
		return

	def push(self, fname, args=None, ip=0):
		""" Pushes a new stack frame onto the call stack
		Arguments
			fname -- Function name
			args -- Arguments
			ip -- Instruction pointer
		"""
		frame 			= StackFrame(Address(fname, ip), self.stack[-1], args)
		frame.thisptr	= self.ip.thisptr

		self.stack.append(frame)
		return

	def pop(self, ndx=-1):
		""" Pops a stack frame from the call stack
		Arguments
			ndx -- Index of the frame to pop (default: -1)
		"""
		self.stack.pop(ndx)
		return

	def map(self, args:list):
		""" Maps the arguments to their values in the current context
		Arguments
			args -- Arguments to map to after resolution
		"""
		ret	= []
		for a in args:
			# If the argument is an expression, evaluate it
			if isinstance(a, Expression):
				ret.append(a.evaluate(self))
				continue

			ret.append( Expression.resolve(self, a) )

		return ret

	def trace(self, msg:str, logging=False):
		""" Logs a trace message
		Arguments
			msg -- Message to log
			logging -- Whether to log the message to file (default: False)
		"""
		print(f'{' '*len(self.stack)}: {msg}')
		if logging:
			self.root.log.append(msg)
		return

	def __str__(self):
		""" A string notation of the object
		"""
		lines	= []
		lines.append(f"{self.ip.address.fname}:{self.ip.address.ip} - Stack depth: {len(self.stack)}, Variables: {self.numvars}{{")

		level	= 0

		# Traverse the stack starting with the lowest level
		while True:
			level		= level + 1	
			if level > len(self.stack):
				break

			scope		= self.stack[-level]
			indent		= ' ' * (level-1)
			for c in scope.vars:
				lines.append(f"{indent}{c} = {scope.vars[c]}")

		
		lines.append(f"}}")
		return '\n'.join(lines)

# Helper class to map variable names to their values in the current context
class VariableMapper(Mapping):
	def __init__(self, ctxt:RuntimeContext):
		""" Constructor
		Arguments
			ctxt -- Runtime memory context
		"""
		self.ctxt = ctxt
		return

	def __getitem__(self, key):
		""" Returns the value of a variable in the current context
		Arguments
			key -- Variable name
		"""
		return self.ctxt.get(key)

	def __iter__(self):
		""" Returns an iterator over the variable names in the current context
		"""
		return None

	def __len__(self):
		""" Returns the number of variables in the current context
		"""
		return len(self.ctxt.numvars)
	
if __name__ == "__main__":
	test = RuntimeContext()

