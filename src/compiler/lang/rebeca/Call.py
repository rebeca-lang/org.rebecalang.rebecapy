#!/usr/bin/python
# Filename: Call.py
# Description: Implementation of the Call class

from compiler.lang.rebeca.RuntimeContext import RuntimeContext as RebecaRuntimeContext
from compiler.lang.program.Call	import Call 
from compiler.lang.program.Statement import Statement
from compiler.lang.program.Expression import Expression

import time, re

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
		return None
			
class Trace(Statement):
	def __init__(self, expr):
		Statement. __init__(self)
		self.expr = expr
		return

	def execute(self, ctxt):
		if isinstance(self.expr, Statement):
			msg = self.expr.execute( ctxt )
		else:
			expr = Expression(self.expr)
			msg  = expr.evaluate( ctxt )
		print(f'{msg}')
		return None

class Format(Statement):
	def __init__(self, expr:str):
		Statement. __init__(self)
		self.expr = expr
		return

	def evaluate(self, ctxt):
		return self.execute( ctxt )
	
	def execute(self, ctxt):
		p = re.compile(r'\{(.+?)\}')
		s = self.expr

		result = []
		prevpos = 0
		for m in p.finditer(s):
			expr 	= m.group(1).strip()

			result.append(s[prevpos:m.start()])
			result.append(f'{eval(expr, None, ctxt.variables)}')

			prevpos = m.end()

		result.append(s[prevpos:])

		return ''.join(result)


if __name__ == "__main__":
	test = Call()
	

