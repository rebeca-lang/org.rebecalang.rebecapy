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
		return Expression.resolve(self.expr, ctxt)

	@staticmethod
	def resolve(a, ctxt):
		if isinstance(a, (bool, int, float, str, type(None))):
			return a

		# If the argument is a tuple, assume it is a variable. 
		if isinstance(a, tuple):
			name	= str(a[1])
			var 	= ctxt.get( name )
			if var is None:
				raise RuntimeError(f'Unresolved reference variable [{name}].')
			
			return var

		if isinstance(a, BinaryOperation):
			return a.evaluate(ctxt)

		# Otherwise, treat it as an expression
		return eval(a, None, ctxt.variables)

	
	def __str__(self):
		return self.expr

class BinaryOperation:
	def __init__(self, lvalue, op, rvalue):
		self.lvalue 	= lvalue
		self.op 		= op
		self.rvalue 	= rvalue
		return

	def evaluate(self, ctxt):
		lvalue = Expression.resolve(self.lvalue, ctxt)
		rvalue = Expression.resolve(self.rvalue, ctxt)

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
		self.rvalue 	= rvalue
		return

	def evaluate(self, ctxt):
		return not Expression.resolve(self.rvalue, ctxt)

if __name__ == "__main__":
	test = Expression()

