#!/usr/bin/python
# Filename: Declaration.py
# Description: Implementation of the Declaration class

from compiler.lang.program.Statement import Statement

class Declaration(Statement):
	def __init__(self, type, lvalue):
		""" Constructor
		Arguments
			type -- data type of the declaration
			lvalue -- left-hand side variable(s) of the declaration
		"""
		Statement.__init__(self)
		self.lvalue		= lvalue
		self.type		= type
		return

	def execute(self, ctxt):
		""" Execute the declaration statement.
		Arguments
			ctxt -- Runtime memory context
		"""
		for n in self.lvalue:
			ctxt.set( n, Statement.default_value(self.type) )
		return None
	
	def __str__(self):
		""" A string notation of the object
		"""
		return f"{self.type} {self.lvalue};"
		

if __name__ == "__main__":
	test = Declaration()

