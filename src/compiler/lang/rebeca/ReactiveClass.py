#!/usr/bin/python
# Filename: ReactiveClass.py
# Description: Implementation of the ReactiveClass class

from compiler.lang.rebeca.MsgServer import MsgServer, TypeInfo as MsgServerType
from compiler.lang.rebeca.LocalFunction import LocalFunction, TypeInfo as LocalFunctionType
from compiler.lang.rebeca.Constructor import Constructor
from compiler.lang.rebeca.Destructor import Destructor
from compiler.lang.rebeca.RuntimeContext import RuntimeContext as RebecaRuntimeContext
from compiler.lang.program.RuntimeContext import RuntimeContext
from compiler.lang.program.Instruction import Instructions

class ReactiveClass:
	def __init__(self, name:str, queue_size:int=-1):
		self.name			= name
		self.ctor			= None
		self.dtor 			= None

		# Default settings
		self.queue_size		= queue_size

		# Class elements
		self.known_rebecs	= []	# Known rebecs list
		self.state_vars		= {}	# State variables
		self.servers		= {}	# Message servers
		self.locals			= {}	# Local functions	
		return

	def constructor(self, instructions:list=None, arglist=None):
		if self.ctor:
			raise RuntimeError(f'Constructor already defined in reactive class [{self.name}].')
		
		self.ctor = Constructor(f'{self.name}.{self.name}', Instructions(instructions), arglist)
		return self

	def destructor(self, instructions:list=None):
		if self.dtor:
			raise RuntimeError(f'Destructor already defined in reactive class [{self.name}].')

		self.dtor = Destructor(f'{self.name}.~{self.name}', Instructions(instructions))
		return self

	def known_rebec(self, names:list, rtype:str):
		for n in names:
			self.known_rebecs.append((n, rtype))
		return self
	
	def state_var(self, names:list, vtype:str):	
		for n in names:
			self.state_vars[n] = vtype
		return self
	
	def msg_server(self, name:str, instructions:list=None, arglist:list=None):
		if name in self.servers:
			raise RuntimeError(f'Message server [{name}] already defined in reactive class [{self.name}].')
		
		if self.__handle_ctor_dtor(name, instructions, arglist):
			return self
		server = MsgServer(f'@{self.name}.{name}', Instructions(instructions), arglist)
		tinfo  = MsgServerType(server)
		self.servers[name] = tinfo
		return self

	def __handle_ctor_dtor(self, name:str, instructions:list=None, arglist:list=None):
		if (name == self.name) or (name == 'initial'):
			if self.ctor:
				raise RuntimeError(f'Constructor already defined in reactive class [{self.name}].')
			self.ctor = Constructor(f'{self.name}.{name}', Instructions(instructions), arglist)
			return True
		
		elif name == f'~{self.name}':
			if self.dtor:
				raise RuntimeError(f'Destructor already defined in reactive class [{self.name}].')
			self.dtor = Destructor(f'{self.name}.{name}', Instructions(instructions))
			return True
		
		return False
		
	def local_function(self, name:str, rtype:str, instructions:list=None, arglist:dict=None):
		if name in self.locals:
			raise RuntimeError(f'Local function [{name}] already defined in reactive class [{self.name}].')
		
		local = LocalFunction(f'{self.name}.{name}', Instructions(instructions), arglist)
		tinfo = LocalFunctionType(local, rtype)
		self.locals[name] = tinfo
		return self
	
	
	def construct(self, inst, ctxt:RuntimeContext, args:list):
		return inst.construct(ctxt, args)

	def invoke(self, ctxt:RuntimeContext, method:str, args):
		tinfo	= self.get_method(method)
		if tinfo is None:
			raise RuntimeError(f'Method [{method}] not found in message server [{self.name}].')
		
		# Invoke the method with the given arguments
		if ctxt is None:
			ctxt = RebecaRuntimeContext()
			
		return tinfo.program.invoke(self, ctxt, args)

		
	def get_method(self, name:str):
		server	= self.servers.get(name, None)
		if server:
			return server
		 
		local	= self.locals.get(name, None) 
		if local:
			return local
		
		return None
	
	def __str__(self):
		lines = []

		queueinfo = ''
		if self.queue_size>-1:
			queueinfo = f'({self.queue_size})'

		# Declare the reactive class
		lines.append(f'reactiveclass {self.name}{queueinfo} {{')

		# Declare known rebecs
		if len(self.known_rebecs)>0:
			lines.append(f'knownrebecs {{')
			for k, v in self.known_rebecs.items():
				lines.append(f' {v} {k} ;')
			lines.append(f'}}')

		# Declare state variables
		if len(self.state_vars)>0:
			lines.append(f'statevars {{')
			for k, v in self.state_vars.items():
				lines.append(f' {v} {k} ;')
			lines.append(f'}}')

		# Declare constructor
		if self.ctor is not None:
			lines.append(f'{self.name}({self.ctor.arglist}) {self.ctor}')

		# Declare message servers
		for name, tinfo in self.servers.items():
			lines.append(f'msgsrv {name}{tinfo.program.__str__()}')

		# Declare local functions
		for name, tinfo in self.locals.items():
			rtype = 'void' if len(tinfo.rtype)==0 else tinfo.rtype[1]
			lines.append(f'{rtype} {name}{tinfo.program.__str__()}')

		lines.append(f'}}')
		return '\n'.join(lines)


if __name__ == "__main__":
	test = ReactiveClass()

