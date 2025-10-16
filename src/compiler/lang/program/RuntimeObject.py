#!/usr/bin/python
# Filename: RuntimeObject.py
# Description: Implementation of the RuntimeObject class

from abc import ABC, abstractmethod

class RuntimeObject(ABC):
	def __init__(self):
		return
	
	@abstractmethod
	def invoke(self, ctxt, method:str, args):
		pass

	@staticmethod
	def dispatch(self, vtbls, method:str, args):
		for v in vtbls:
			pfn	= v.get(method, None)
			if pfn is not None:
				return pfn(*args)

		raise RuntimeError(f'Method {method} not found in class \'{self.__class__.__name__}\'')

		

if __name__ == "__main__":
	test = RuntimeObject()

