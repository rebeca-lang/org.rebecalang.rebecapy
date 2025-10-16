#!/usr/bin/python
# Filename: Return.py
# Description: Implementation of the Return class

from compiler.lang.program.Statement import Statement

# Subclass representing a return statement
class Return(Statement):
	def __init__(self, expr):
		Statement.__init__(self)
		self.expr	= expr
		return

	def evaluate(self, ctxt, expr):
		return ctxt.get(expr)
	
	def execute(self, runtime, ctxt, frame):
		result	= ctxt.evaluate(self.expr)
		ctxt.ax	= result
		ctxt.pop()
		return True

	def __str__(self):
		return f'return {self.expr}'

if __name__ == "__main__":
	test = Return()

