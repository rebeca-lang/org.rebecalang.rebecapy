#!/usr/bin/python
# Filename: SubProgram.py
# Description: Implementation of the SubProgram class

from compiler.lang.program.Instruction import Instructions
from compiler.lang.program.Program import Program
from compiler.lang.program.RuntimeContext import RuntimeContext

# A module for a reusable sequence of instructions that can be invoked with a name and arguments.
class SubProgram(Program):
	def __init__(self, name:str, instructions:Instructions=None, arglist=None):
		Program.__init__(self, name, instructions, arglist)
		return
	

		

if __name__ == "__main__":
	test = SubProgram()

