#!/usr/bin/python
# Filename: While.py
# Description: Implementation of the While class

from compiler.lang.program.LoopBlock import LoopBlock

# Subclass representing a while loop
class While(LoopBlock):
	def __init__(self, condition, statements):
		LoopBlock.__init__(self, statements)
		self.statements	= statements
		self.condition	= condition
		return

	def evaluate(self, ctxt):
		return ctxt.evaluate(self.condition)

	def execute(self, ctxt):
		while self.evaluate(ctxt):
			LoopBlock.execute(self, ctxt)
		return True

	def __str__(self):
		result = "while ( " + str(self.condition) + " ) {\n"
		for instr in self.instructions:
			result += "    " + str(instr) + "\n"
		result += "}"
		return result
		

if __name__ == "__main__":
	test = While( t)

