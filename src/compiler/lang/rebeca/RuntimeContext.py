#!/usr/bin/python
# Filename: RuntimeContext.py
# Description: Implementation of the RuntimeContext class

from compiler.lang.program.RuntimeContext import RuntimeContext as RuntimeContextBase

class RuntimeContext(RuntimeContextBase):
	def __init__(self, module, factory):
		""" Constructor
		Arguments
			module -- Rebeca module
			factory -- Factory for creating actors and objects
		"""
		RuntimeContextBase.__init__(self)

		# Server module
		self.module		= module

		# List of server instances
		self.instances	= {}		# List of instantiated instances
		self.bound		= False		# Chek if the instances are initialized
		self.factory	= factory
		self.pending	= True
		return

	@property
	def stacklen(self):
		""" Size of the stack
		"""
		return len(self.stack)

	def fork(self):
		""" Forks the current runtime context
		"""
		newctxt 			= self.clone()

		while len(newctxt.stack) != 1:
			newctxt.stack.pop(0)

		return newctxt

	def clone(self):
		""" Clones the current runtime context
		"""
		newctxt 			= RuntimeContext(self.module, self.factory)

		# Clone base context
		RuntimeContextBase.copy(self, newctxt)

		# Clone propertes
		newctxt.module 		= self.module
		newctxt.instances	= self.instances.copy()
		return newctxt
	
	def create(self, module, argv:dict=None):
		""" Creates a runtime context from a module
		Arguments
			module -- Rebeca module to create a context from
			argv -- Arguments for the main rebec
		"""
		for env in module.envs:
			env.execute(self)

		if module.main:
			module.main.create(self, argv)
			
		# bind all instancees
		self.bind()
		return

	def destroy(self):
		""" Destroys the runtime context
		"""
		for i in self.instances.values():
			i.destroy(self)
		self.instances.clear()
		return

	def bind(self):
		""" Binds the rebec instances in the context
		"""
		# Bind known rebecs from the global context. All instances 
		# must be created first before they can be run. This is 
		# done only once.
		if self.bound == False:
			for inst in self.instances.values():
				inst.construct(self)
			self.bound = True
		return
	
	def step(self):
		""" Runs a single step of the runtime context
		"""
		if self.bound == False:
			self.bind()

		hasrunnable	= False

		# Step all runnable instances
		for i in self.instances.values():
			if i.runnable == False:
				continue

			i.step(self)

			# Are there still runnable instances?
			if i.msgcount > 0:
				hasrunnable	= True

		self.pending	= hasrunnable
		return

	def get(self, name):
		""" Retrieves a variable from the context
		Arguments
			name -- Name of the variable
		"""
		# Check in the current instance first
		thisptr = self.ip.thisptr
		if thisptr is not None:
			value = thisptr.kr.get( name, None)
			if value is not None:
				return value

		value = self.instances.get( name, None)
		if value is not None:
			return value

		return RuntimeContextBase.get(self, name)

	def create_actor(self, rc, name:str, idents:list=None, params:list=None):
		""" Creates a new actor instance
		Arguments
			rc -- Runtime context
			name -- Name of the actor
			idents -- Identifiers
			params -- Parameter list
		"""
		return self.factory.create_actor( self, rc, name, idents, params )

	def create_object(self, type:str):			
		""" Creates a runtime object
		Arguments
			type -- Object type
		"""
		return self.factory.create_object(self, type)

if __name__ == "__main__":
	test = RuntimeContext()

