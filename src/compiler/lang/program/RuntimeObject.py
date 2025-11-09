#!/usr/bin/python
# Filename: RuntimeObject.py
# Description: Implementation of the RuntimeObject class

from abc import ABC, abstractmethod

class RuntimeObject(ABC):
	def __init__(self):
		""" Constructor
		"""
		return
	
	@abstractmethod
	def invoke(self, ctxt, method:str, args):
		""" Invoke a method on the object
		Arguments
			ctxt -- Runtime memory context
			method -- Method name
			args -- arguments
		"""
		pass

	@staticmethod
	def dispatch(self, vtbls, method:str, args):
		""" Dispatch a method call to the appropriate method in the vtable
		Arguments
			vtbls -- #TODO
			method -- Method name
			args -- arguments
		"""
		for v in vtbls:
			pfn	= v.get(method, None)
			if pfn is not None:
				return pfn(*args)

		raise RuntimeError(f'Method {method} not found in class \'{self.__class__.__name__}\'')

		

if __name__ == "__main__":
	test = RuntimeObject()

