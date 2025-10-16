#!/usr/bin/python
# Filename: Main.py
# Description: Implementation of the Main class

from compiler.lang.rebeca.SubProgram import SubProgram
from compiler.lang.rebeca.Instance import Instance
from compiler.lang.program.Instruction import Instructions

class Main(SubProgram):
	def __init__(self, instructions:Instructions=None, arglist=None):
		SubProgram.__init__(self, 'main', instructions, arglist)
		return
	
	def declare(self, inst):
		self.append( Instance(inst[0], inst[1], inst[2], inst[3]) )
		return

	def create(self, ctxt):
		self.run(ctxt)
		return
	
	def __str__(self):		
		return f'main{SubProgram.__str__(self)}'



class TypeInfo:
	def __init__(self, program:Main):
		self.program	= program
		return

	@property
	def name(self):
		return self.program.name
		

if __name__ == "__main__":
	test = Main()

