#!/usr/bin/python
# Filename: Expression.py
# Description: Implementation of the Expression class

# Class representing an expression to be evaluated
class Expression:
	def __init__(self, expr, debug=False):
		self.expr 	= expr
		self.debug	= debug
		return

	def evaluate(self, ctxt):
		if isinstance(self.expr, (bool, int, float, type(None))):
			return self.expr

		# If the argument is a tuple, assume it is a string. 
		# return the value
		if isinstance(self.expr, tuple):
			return self.expr[1]

		return eval(self.expr, None, ctxt.variables)

	def __str__(self):
		return self.expr

if __name__ == "__main__":
	test = Expression()

