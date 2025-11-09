#!/usr/bin/python
# Filename: Assignment.py
# Description: Implementation of the Assignment class

from compiler.lang.program.Statement import Statement
from compiler.lang.program.Expression import Expression

		
class Assignment(Statement):
	def __init__(self, lvalue, rvalue, typename=None):
		""" Constructor
		Arguments
			lvalue -- Variable to assign to
			rvalue -- Value expression to assign
			typename -- Type of the variable
		"""
		Statement.__init__(self)
		
		self.lvalue		= lvalue
		self.declare 	= True if typename else False
		self.type		= typename

		if isinstance(rvalue, Statement):
			self.rvalue		= rvalue
		else:
			self.rvalue		= rvalue if type(rvalue) is Expression else Expression(rvalue)

		return

	def evaluate(self, ctxt):
		""" Executes the statement
		Arguments
			ctxt -- Runtime memory context
		"""
		return self.execute(ctxt)
	
	def execute(self, ctxt):
		""" Executes the statement
		Arguments
			ctxt -- Runtime memory context
		"""
		if self.declare:
			ctxt.set(self.lvalue, None)

		result	= self.rvalue.evaluate(ctxt)

		ctxt.set(self.lvalue, result)
		ctxt.ax	= result
		return ctxt.ax
	
	def __str__(self):
		""" A string notation of the object
		"""
		return f"{self.lvalue} = {self.rvalue.__str__()};"
		

if __name__ == "__main__":
	test = Assignment("x", "5 + 3")
	test.execute(None)

