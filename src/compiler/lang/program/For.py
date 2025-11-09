#!/usr/bin/python
# Filename: For.py
# Description: Implementation of the For class

from compiler.lang.program.LoopBlock import LoopBlock
from compiler.lang.program.Instruction import Instruction

# Subclass representing a for loop
class For(LoopBlock):
	def __init__(self, instructions, start, cond, step):
		""" Constructor
		Arguments
			instructions -- Instructions to execute within the loop
			start -- Initial condition/setup of the loop
			cond -- End condition of the loop
			step -- Step to increment the loop variable
		"""
		LoopBlock.__init__(self, instructions)
		self.start	= start
		self.step 	= step
		self.cond	= cond

		self.index	= start
		return

	
	def execute(self, ctxt):
		""" Execute the loop.
		Arguments
			ctxt -- Runtime memory context
		"""
		# Reset the start state
		self.start.evaluate(ctxt)

		while self.cond.evaluate(ctxt):
			# Execute loop body
			LoopBlock.execute(self, ctxt)

			# Set loop variable in local context
			self.step.evaluate(ctxt)
		
		return None

	def __str__(self):
		""" A string notation of the object
		"""
		lines = []
		lines.append( f'for( {str(self.start)} {self.cond}; {self.step} ){{' )
		lines.append( '\n'.join(Instruction.argstostring(self.instructions)) )
		lines.append( f'}}\n' )
		return '\n'.join(lines)

if __name__ == "__main__":
	test = For()

