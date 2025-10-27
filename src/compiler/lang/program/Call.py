#!/usr/bin/python
# Filename: Call.py
# Description: Implementation of the Call class

from compiler.lang.program.Statement import Statement
from compiler.lang.program.Expression import Expression
from compiler.lang.program.Instruction import Instruction

class Call(Statement):
	def __init__(self, method, args=None):
		Statement.__init__(self)

		if len(method) > 1:
			self.object	= Call.__joincall(method[:-1])
			self.method	= method[-1][1]
			self.call	= f'{self.object}.{self.method}'
		else:
			self.object	= None
			self.method	= method[0][1]
			self.call	= self.method

		self.args	= [Expression(arg) for arg in args] if args else []
		return

	def __joincall(parts):
		call 	= []
		for p in parts:
			call.append(p[1] if isinstance(p, tuple) else p)
		return '.'.join(call)
	
	
	def evaluate(self, ctxt):
		return self.execute(ctxt)
	
	def execute(self, ctxt):
		if self.object is None:
			return self.__call_subroutine(ctxt)
		
		obj = ctxt.get(self.object)
		if obj is None:
			self.throw(f"Object '{self.object}' not found.")
		
		return self.__call_object(ctxt, obj)

			
	def __call_object(self, ctxt, obj):
		try:
			return obj.invoke( ctxt, self.method, ctxt.map(self.args) )
		except Exception as e:
			self.throw( str(e) )
		
	def __call_subroutine(self, ctxt):
		func 	= ctxt.get(self.method)
		if func is None:
			raise Exception(f"Function '{self.method}' not found.")

		
		args	= []

		for arg in self.args:
			args.append(arg.evaluate(ctxt))

		# Push a new stack frame
		ctxt.push( self.call )
		
		# Invoke the function
		ret	= func.execute( ctxt, ctxt.map(self.args) )

		# Pop the stack frame
		ctxt.pop()

		# Set the return value in the accumulator
		ctxt.ax = ret
		return ret
		
	def __str__(self):
		arglist	= Instruction.argstostring(self.args)
		return f'{self.method}({','.join(arglist)})'

if __name__ == "__main__":
	test = Call()

