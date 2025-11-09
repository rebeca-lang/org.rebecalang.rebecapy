#!/usr/bin/python
# Filename: Statement.py
# Description: Implementation of the Statement class

from compiler.lang.program.Instruction import Instruction

# Base class for all statements
class Statement(Instruction):
	def __init__(self):
		""" Constructor
		"""
		Instruction.__init__(self)
		return
	
	@staticmethod
	def default_value(type:str):
		""" Get the default value for a given type
		Arguments
			type -- Type name
		"""
		return {
					'boolean':False,
					'int':0,
					'float':0.0, 
					'double':0.0, 
					'byte':b'\0',
					'string':''
				}.get(type, None)
		

if __name__ == "__main__":
	test = Statement()

