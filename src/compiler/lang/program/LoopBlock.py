#!/usr/bin/python
# Filename: LoopBlock.py
# Description: Implementation of the LoopBlock class

from compiler.lang.program.Instruction import Instruction

# Subclass representing a loop block of instructions
class LoopBlock(Instruction):
	def __init__(self, instructions=None):
		Instruction.__init__(self)
		self.instructions	= instructions if instructions is not None else []
		return

	def append(self, instruction):
		self.instructions.append(instruction)
		return

	def execute(self, ctxt):
		for instr in self.instructions:
			instr.execute(ctxt)
			
		return
		

if __name__ == "__main__":
	test = LoopBlock()

