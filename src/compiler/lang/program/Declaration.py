#!/usr/bin/python
# Filename: Declaration.py
# Description: Implementation of the Declaration class

from compiler.lang.program.Statement import Statement

class Declaration(Statement):
	def __init__(self, type, lvalue):
		Statement.__init__(self)
		self.lvalue		= lvalue
		self.type		= type
		return

	def execute(self, ctxt):
		for n in self.lvalue:
			ctxt.set( n, Statement.default_value(self.type) )
		return None
	
	def __str__(self):
		return f"{self.type} {self.lvalue};"
		

if __name__ == "__main__":
	test = Declaration()

