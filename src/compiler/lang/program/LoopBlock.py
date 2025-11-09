#!/usr/bin/python
# Filename: LoopBlock.py
# Description: Implementation of the LoopBlock class

from compiler.lang.program.Instruction import Instruction

# Subclass representing a loop block of instructions
class LoopBlock(Instruction):
	def __init__(self, instructions=None):
		""" Constructor
		Arguments
			instructions -- Instructions to execute within the block
		"""
		Instruction.__init__(self)
		self.instructions	= instructions if instructions is not None else []
		return

	def append(self, instruction):
		""" Append an instruction to the block
		Arguments
			instruction -- Instruction to append
		"""
		self.instructions.append(instruction)
		return

	def execute(self, ctxt):
		""" Execute the loop block.
		Arguments
			ctxt -- Runtime memory context
		"""
		for instr in self.instructions:
			instr.execute(ctxt)
			
		return
		

if __name__ == "__main__":
	test = LoopBlock()

