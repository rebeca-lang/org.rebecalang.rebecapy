#!/usr/bin/python
# Filename: Composite.py
# Description: Implementation of the Composite class

from compiler.lang.program.Instruction import Instruction

class Composite:
	def __init__(self):
		""" Constructor
		"""
		Instruction.__init__(self)
		return

	def evaluate(self, ctxt):
		""" Evaluate the composite instruction.
		Arguments
			ctxt -- Runtime memory context
		"""
		return None

		

if __name__ == "__main__":
	test = Composite()

