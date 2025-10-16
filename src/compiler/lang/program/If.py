#!/usr/bin/python
# Filename: If.py
# Description: Implementation of the If class

from compiler.lang.program.Instruction import Instruction

# Subclass representing an if statement with a condition and instructions
class If(Instruction):
	def __init__(self, condition, instructions=None, elseinstructions=None):
		Instruction.__init__(self)
		self.instructions	= instructions if instructions is not None else []
		self.condition		= condition
		self.elsecond		= elseinstructions if elseinstructions is not None else []
		return

	def execute(self, ctxt):
		result	= eval(self.condition, None, ctxt.variables)
		if result:
			for instr in self.instructions:
				instr.execute(ctxt)
		return None

	def __str__(self):
		stmts	= Instruction.argstostring(self.instructions)

		return f'if( {str(self.condition)} ){{\n{'\n'.join(stmts)}\n}}\n'

if __name__ == "__main__":
	test = If()

