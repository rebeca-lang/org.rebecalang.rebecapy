#!/usr/bin/python
# Filename: Instance.py
# Description: Implementation of the Instance class

from compiler.lang.rebeca.RuntimeContext import RuntimeContext as RebecaRuntimeContext
from compiler.lang.program.Instruction import Instruction
from compiler.lang.program.RuntimeContext import RuntimeContext

# Subclass representing an instance declaration
class Instance(Instruction):
	def __init__(self, type, name, identifiers, params, callback=None):
		""" Constructor
		Arguments
			type -- Type of the instance
			name -- Name of the instance
			identifiers -- List of identifiers
			params -- Parameters list
			callback -- Callback function after execution
		"""
		Instruction.__init__(self)
		self.type		= type
		self.name		= name
		self.idents		= [i[1] if isinstance(i, tuple) else i for i in identifiers]
		self.params		= params
		self.callback	= callback
		return

	def execute(self, ctxt:RuntimeContext):
		""" Executes the instance creation
		Arguments
			ctxt -- Runtime memory context
		"""
		# ctxt.trace(f'Creating instance: {self.name} of type {self.type}')
		rctxt:RebecaRuntimeContext	= ctxt
		rc							= rctxt.module.get(self.type)
		if rc is None:
			raise RuntimeError(f'Reactive class [{self.type}] not found to create instance [{self.name}].')

		# Dynamic parameter mapping
		params	= ctxt.map(self.params)

		rctxt.instances[self.name]	= ctxt.create_actor( rc, self.name, self.idents, params )
		return None

	def __str__(self):
		""" A string notation of the object
		"""
		arglist	= Instruction.argstostring(self.params)
		return f'{self.type} {self.name}({','.join(self.idents)}):({','.join(arglist)})'

if __name__ == "__main__":
	test = Instance()

