#!/usr/bin/python
# Filename: Expression.py
# Description: Implementation of the Expression class

import re

# Class representing an expression to be evaluated
class Expression:
	def __init__(self, expr, debug=False):
		""" Constructor
		Arguments
			expr -- Expression string
			debug -- Enable debugging
		"""
		self.expr 	= expr
		self.debug	= debug
		return

	def evaluate(self, ctxt):
		""" Evaluate the expression.
		Arguments
			ctxt -- Runtime memory context
		"""
		return Expression.resolve(ctxt, self.expr)

	@staticmethod
	def resolve(ctxt, a):
		""" Resolve the expression.
		Arguments
			ctxt -- Runtime memory context
			a -- Expression to resolve
		"""
		if isinstance(a, (bool, int, float, str, type(None))):
			return a

		if isinstance(a, BinaryOperation):
			return a.evaluate(ctxt)

		# If the argument is a tuple, assume it is a variable. 
		if isinstance(a, tuple):
			name	= str(a[1])
			var 	= ctxt.get( name )
			if var is None:
				raise RuntimeError(f'Unresolved reference variable [{name}].')
			
			return var

		# Otherwise, treat it as an expression
		return eval(a, None, ctxt.variables)

	
	def __str__(self):
		""" A string notation of the object
		"""
		return self.expr

	
class BinaryOperation:
	def __init__(self, lvalue, op, rvalue):
		""" Constructor
		Arguments
			lvalue -- Left-hand side value
			op -- operation code
			rvalue -- Right-hand side value
		"""
		self.lvalue 	= lvalue
		self.op 		= op
		self.rvalue 	= rvalue
		return

	def evaluate(self, ctxt):
		""" Evaluate the binary operation.
		Arguments
			ctxt -- Runtime memory context
		"""
		lvalue = Expression.resolve(ctxt, self.lvalue)
		rvalue = Expression.resolve(ctxt, self.rvalue)

		if self.op == '+':
			return lvalue + rvalue
		elif self.op == '-':
			return lvalue - rvalue
		elif self.op == '*':
			return lvalue * rvalue
		elif self.op == '/':
			return lvalue / rvalue
		elif self.op == '==':
			return lvalue == rvalue
		elif self.op == '!=':
			return lvalue != rvalue
		elif self.op == '<':
			return lvalue < rvalue
		elif self.op == '>':
			return lvalue > rvalue
		elif self.op == '<=':
			return lvalue <= rvalue
		elif self.op == '>=':
			return lvalue >= rvalue
		elif self.op == 'and':
			return lvalue and rvalue
		elif self.op == 'or':
			return lvalue or rvalue
		elif self.op == 'xor':
			return lvalue ^ rvalue
		else:
			raise RuntimeError(f'Unsupported opcode {self.op}')
		return

class NotOperation:
	def __init__(self, op, rvalue):
		""" Constructor
		Arguments
			op -- Operation code
			rvalue -- Right-hand side value
		"""
		self.rvalue 	= rvalue
		return

	def evaluate(self, ctxt):
		""" Evaluate the NOT operation.
		Arguments
			ctxt -- Runtime memory context
		"""
		return not Expression.resolve(self.rvalue, ctxt)

if __name__ == "__main__":
	test = Expression()

