#!/usr/bin/python
# Filename: Assignment.py
# Description: Implementation of the Assignment class

from compiler.lang.program.Statement import Statement
from compiler.lang.program.Expression import Expression

		
class Assignment(Statement):
	def __init__(self, lvalue, rvalue, type=None):
		Statement.__init__(self)
		
		self.lvalue		= lvalue
		self.rvalue		= Expression(rvalue)
		self.declare 	= True if type else False
		self.type		= type

		if isinstance(rvalue, Statement):
			self.rvalue		= rvalue
		else:
			self.rvalue		= Expression(rvalue)

		return

	def evaluate(self, ctxt):
		return self.execute(ctxt)
	
	def execute(self, ctxt):
		if self.declare:
			ctxt.set(self.lvalue, None)

		result	= self.rvalue.evaluate(ctxt)

		ctxt.set(self.lvalue, result)
		ctxt.ax	= result
		return ctxt.ax
	
	def __str__(self):
		return f"{self.lvalue} = {self.rvalue.__str__()};"
		

if __name__ == "__main__":
	test = Assignment("x", "5 + 3")
	test.execute(None)

