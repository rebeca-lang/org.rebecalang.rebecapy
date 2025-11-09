#!/usr/bin/python
# Filename: Constructor.py
# Description: Implementation of the Constructor class

from compiler.lang.rebeca.SubProgram import SubProgram
from compiler.lang.program.Instruction import Instructions

class Constructor(SubProgram):
	def __init__(self, name, instructions:Instructions=None, arglist=None):
		""" Constructor
		Arguments
			name -- Internal name of the constructor method
			instructions -- List of instructions to be executed
			arglist -- List of constructor arguments
		"""
		SubProgram.__init__(self, name, instructions, arglist)
		return

		

if __name__ == "__main__":
	test = Constructor()

