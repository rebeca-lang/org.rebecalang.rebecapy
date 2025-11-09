#!/usr/bin/python
# Filename: Return.py
# Description: Implementation of the Return class

from compiler.lang.program.Statement import Statement

# Subclass representing a return statement
class Return(Statement):
	def __init__(self, expr):
		""" Constructor
		Arguments
			expr -- Expression to evaluate and return
		"""
		Statement.__init__(self)
		self.expr	= expr
		return

	def evaluate(self, ctxt, expr):
		""" Evaluate the return statement.
		Arguments
			ctxt -- Runtime memory context
			expr -- Expression to evaluate
		"""
		return ctxt.get(expr)
	
	def execute(self, runtime, ctxt, frame):
		""" Executes the return statement
		Arguments
			runtime -- Runtime environment
			ctxt -- Runtime memory context
			frame -- Current stack frame
		"""
		result	= ctxt.evaluate(self.expr)
		ctxt.ax	= result
		ctxt.pop()
		return True

	def __str__(self):
		""" A string notation of the object
		"""
		return f'return {self.expr}'

if __name__ == "__main__":
	test = Return()

