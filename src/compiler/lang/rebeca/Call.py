#!/usr/bin/python
# Filename: Call.py
# Description: Implementation of the Call class

from compiler.lang.rebeca.RuntimeContext import RuntimeContext as RebecaRuntimeContext
from compiler.lang.program.Call	import Call 
from compiler.lang.program.Statement import Statement
from compiler.lang.program.Expression import Expression

import time

class SendMessage(Call):
	def __init__(self, method, args=None):
		Call. __init__(self, method, args)
		return

class Delay(Statement):
	def __init__(self, millsec=None):
		Statement. __init__(self)
		self.millsec = millsec
		return

	def execute(self, ctxt):
		if self.millsec is not None:
				time.sleep(self.millsec / 1000.0)
		return
			
class Trace(Statement):
	def __init__(self, expr:str):
		Statement. __init__(self)
		self.expr = expr
		return

	def execute(self, ctxt):
		if isinstance(self.expr, str): 
			msg = self.expr
		elif isinstance(self.expr, Statement):
			msg = self.expr.execute( ctxt )
		else:
			expr = Expression(self.expr)
			msg  = expr.evaluate( ctxt )
		print(f'{msg}')
		return
		
if __name__ == "__main__":
	test = Call()

