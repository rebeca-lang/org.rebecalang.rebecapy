#!/usr/bin/python
# Filename: MsgServer.py
# Description: Implementation of the MsgServer class

from compiler.lang.rebeca.SubProgram import SubProgram
from compiler.lang.program.Instruction import Instructions

	
class MsgServer(SubProgram):
	def __init__(self, name:str, instructions:Instructions=None, arglist=None):
		SubProgram.__init__(self, name, instructions, arglist)
		return

class TypeInfo:
	def __init__(self, program:MsgServer):
		self.program	= program
		return
	
	@property
	def name(self):
		return self.program.name
	
if __name__ == "__main__":
	test = MsgServer()

