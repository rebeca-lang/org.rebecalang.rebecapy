#!/usr/bin/python
# Filename: Destructor.py
# Description: Implementation of the Destructor class

from compiler.lang.rebeca.SubProgram import SubProgram
from compiler.lang.program.Instruction import Instructions

class Destructor(SubProgram):
	def __init__(self, name, instructions:Instructions=None):
		""" Constructor
		Arguments
			name -- Internal name of the destructor method
			instructions -- List of instructions to be executed
		"""
		SubProgram.__init__(self, name, instructions)
		return

		

if __name__ == "__main__":
	test = Destructor()

