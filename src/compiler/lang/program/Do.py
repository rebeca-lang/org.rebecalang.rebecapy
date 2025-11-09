#!/usr/bin/python
# Filename: Do.py
# Description: Implementation of the Do class

from compiler.lang.program.LoopBlock import LoopBlock

# Subclass representing a do-while loop
class Do(LoopBlock):
	def __init__(self, condition, instructions=None):
		""" Constructor
		Arguments
			condition -- Condition for the loop
			instructions -- Instructions to execute within the loop
		"""
		LoopBlock.__init__(self, instructions)
		self.condition		= condition
		return

	def evaluate(self, ctxt):
		""" Evaluate the loop condition.
		Arguments
			ctxt -- Runtime memory context
		"""
		return ctxt.evaluate(self.condition)

	def execute(self, ctxt):
		""" Execute the loop.
		Arguments
			ctxt -- Runtime memory context
		"""
		while True:
			LoopBlock.execute(self, ctxt)
					
			if self.evaluate(ctxt):
				continue
			else:
				break

		return True

	def __str__(self):
		""" A string notation of the object
		"""
		result	= "do{\n"
		for instr in self.instructions:
			result	+= "\t" + str(instr).replace("\n", "\n\t") + "\n"
		result	+= "}while (" + self.condition + ")\n"
		return result

if __name__ == "__main__":
	test = Do()

