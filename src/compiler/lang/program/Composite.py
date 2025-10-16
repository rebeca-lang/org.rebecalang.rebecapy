#!/usr/bin/python
# Filename: Composite.py
# Description: Implementation of the Composite class

from compiler.lang.program.Instruction import Instruction

class Composite:
	def __init__(self):
		Instruction.__init__(self)
		return

	def evaluate(self, ctxt):
		return None

		

if __name__ == "__main__":
	test = Composite()

