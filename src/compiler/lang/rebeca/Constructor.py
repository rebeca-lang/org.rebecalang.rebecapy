#!/usr/bin/python
# Filename: Constructor.py
# Description: Implementation of the Constructor class

from compiler.lang.rebeca.SubProgram import SubProgram
from compiler.lang.program.Instruction import Instructions

class Constructor(SubProgram):
	def __init__(self, name, instructions:Instructions=None, arglist=None):
		SubProgram.__init__(self, name, instructions)
		return

		

if __name__ == "__main__":
	test = Constructor()

