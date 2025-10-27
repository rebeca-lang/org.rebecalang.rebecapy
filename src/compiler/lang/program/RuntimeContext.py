#!/usr/bin/python
# Filename: RuntimeContext.py
# Description: Implementation of the RuntimeContext class

from collections.abc import Mapping
from compiler.lang.program.Expression import Expression

# Represents an address in the program (function name and instruction pointer)
class Address:
	def __init__(self, fname, ip):
		self.fname	= fname		# function name
		self.ip 	= ip		# instruction pointer
		return
	
	def __str__(self):
		return f"{self.fname}:{self.ip}"

# Represents the runtime context of the program execution	
class StackFrame:
	def __init__(self, address:Address, return_address:Address, vars=None):
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
		instruction	= ctxt.get(self.address.ip)
		if instruction is None:
			return False
		
		instruction.execute(runtime, ctxt, self)
		return True
	
	def __str__(self):
		return str(self.address)


# Main class managing the runtime context, including the call stack and variable scopes
class RuntimeContext:
	def __init__(self, parent=None):
		self.stack 			= []
		self.instruction	= None
		self.ax				= None		# accumulator
		self.parent			= parent
		self.log			= []

		self.stack.append(StackFrame(Address("global", 1), None))
		return

	def copy(self, rhs):
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
		if self.ip.vars.get(name) is not None:
			raise RuntimeError(f'Variable [{name}] already exists in the current scope.')

		self.ip.vars[name] = value
		return

	def set_self(self, obj):
		ip				= self.ip

		# Set the 'self' pointer in the local context
		ip.thisptr 		= obj

		# Set the instance in the map so it 
		# can be accessed by eval()
		ip.vars['self'] = obj
		return
	
	def set(self, name, value):
		ip 		= self.ip

		if ip.thisptr is not None:
			if name in ip.thisptr.vars:
				ip.thisptr.vars[name]	= value
				return
			
		ip.vars[name] = value
		return

	def test(self):
		assert isinstance( self.ip.vars, dict)

	def get(self, name):		
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
		# Execute the current instruction
		current			= self.stack[-1]
		if current.execute(self, ctxt) == False:
			return False

		# Move the address to the next instruction
		current.address.ip += 1
		return True
	
	@property
	def ip(self):
		return self.stack[-1]

	@property
	def sp(self):
		return len(self.stack)

	@property
	def numvars(self):
		count = 0
		for f in self.stack:
			count += len(f.vars)
		return count

	@property
	def root(self):
		next = self
		while next.parent is not None:
			next = next.parent

		return next

	@property
	def variables(self):
		return VariableMapper(self)

	@property
	def callstack(self):
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
		return self.ip.thisptr
	
	def next(self):
		self.stack[-1].address.ip += 1
		return

	def push(self, fname, args=None, ip=0):
		frame 			= StackFrame(Address(fname, ip), self.stack[-1], args)
		frame.thisptr	= self.ip.thisptr

		self.stack.append(frame)
		return

	def pop(self, ndx=-1):
		self.stack.pop(ndx)
		return

	def map(self, args:list):
		ret	= []
		for a in args:
			# If the argument is an expression, evaluate it
			if isinstance(a, Expression):
				ret.append(a.evaluate(self))
				continue

			ret.append( Expression.resolve(a, self) )

		return ret

	def trace(self, msg:str, logging=False):
		print(f'{' '*len(self.stack)}: {msg}')
		if logging:
			self.root.log.append(msg)
		return

	def __str__(self):
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
		self.ctxt = ctxt
		return

	def __getitem__(self, key):
		return self.ctxt.get(key)

	def __iter__(self):
		return None

	def __len__(self):
		return len(self.ctxt.numvars)
	
if __name__ == "__main__":
	test = RuntimeContext()

