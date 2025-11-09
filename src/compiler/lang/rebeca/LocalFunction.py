#!/usr/bin/python
# Filename: LocalFunction.py
# Description: Implementation of the LocalFunction class

from compiler.lang.rebeca.SubProgram import SubProgram
from compiler.lang.program.Instruction import Instructions

class LocalFunction(SubProgram):
	def __init__(self, name:str, instructions:Instructions=None, arglist=None):
		""" Constructor
		Arguments
			name -- Name of the local function
			instructions -- Instructions of the local function
			arglist -- Argument list of the local function
		"""
		SubProgram.__init__(self, name, instructions, arglist)
		return
			
class TypeInfo:
	def __init__(self, program:LocalFunction, rtype:str):
		""" Constructor
		Arguments
			program -- LocalFunction object
			rtype -- Return type of the local function
		"""
		self.program	= program
		self.rtype		= rtype
		return

	@property
	def name(self):
		""" Name of the local function
		"""
		return self.program.name

if __name__ == "__main__":
	test = LocalFunction()

