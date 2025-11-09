#!/usr/bin/python
# Filename: NoOperation.py
# Description: Implementation of the NoOperation class

from compiler.lang.program.Instruction import Instruction

# Subclass representing a no-operation instruction
class NoOperation(Instruction):
	def __init__(self):
		""" Constructor
		"""
		Instruction.__init__(self)
		return

	def evaluate(self, ctxt):
		""" Evaluate the no-operation instruction.
		Arguments
			ctxt -- Runtime memory context
		"""
		return None
		

if __name__ == "__main__":
	test = NoOperation()

