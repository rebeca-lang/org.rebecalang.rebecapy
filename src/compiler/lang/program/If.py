#!/usr/bin/python
# Filename: If.py
# Description: Implementation of the If class

from compiler.lang.program.Instruction import Instruction

# Subclass representing an if statement with a condition and instructions
class If(Instruction):
	def __init__(self, condition, instructions=None, elseinstructions=None):
		""" Constructor
		Arguments
			condition -- Condition for the if statement
			instructions -- Instructions to execute if the condition is true
			elseinstructions -- Instructions to execute if the condition is false
		"""
		Instruction.__init__(self)
		self.instructions	= instructions if instructions is not None else []
		self.condition		= condition
		self.elsecond		= elseinstructions if elseinstructions is not None else []
		return

	def execute(self, ctxt):
		""" Execute the if statement.
		Arguments
			ctxt -- Runtime memory context
		"""
		result	= self.condition.evaluate(ctxt)
		if result:
			for instr in self.instructions:
				instr.execute(ctxt)
		return None

	def __str__(self):
		""" A string notation of the object
		"""
		stmts	= Instruction.argstostring(self.instructions)

		return f'if( {str(self.condition)} ){{\n{'\n'.join(stmts)}\n}}\n'

if __name__ == "__main__":
	test = If()

