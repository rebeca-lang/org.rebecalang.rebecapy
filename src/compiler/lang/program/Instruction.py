#!/usr/bin/python
# Filename: Instruction.py
# Description: Implementation of the Instruction class

from compiler.lang.program.RuntimeContext import RuntimeContext
from abc import ABC, abstractmethod

# Base class for all instructions
class Instruction(ABC):
	def __init__(self, statements=None):
		self.ip			= 0	
		return
	
	def reset(self):
		self.ip	= 0
		return self
	
	def location(self, context):
		self.module		= context[0]
		self.line		= context[1]
		return self

	def throw(self, msg):
		raise RuntimeError(f'Runtime error at {self.module}({self.line}) : {msg}')
	
	@abstractmethod
	def execute(self, runtime, ctxt, frame):
		pass

	@staticmethod
	def argstostring(args):
		arglist	= []
		for a in args:
			arglist.append(str(a))
		return arglist


# Subclass representing a block of instructions
class Instructions(Instruction):
	def __init__(self, instructions=None):
		Instruction.__init__(self)
		self.instructions	= instructions if instructions is not None else []
		return

	def append(self, instruction):
		self.instructions.append(instruction)
		return

	def execute(self, ctxt:RuntimeContext, scope:str, args=None):
		# Add the function name and arguments to the context stack
		ctxt.push(scope, args)
		for i in self.instructions:
			i.execute(ctxt)

		# Pop the stack frame
		ctxt.pop()
		return None

	def __str__(self):
		lines = [str(i) for i in self.instructions]
		return '\n'.join(lines)

if __name__ == "__main__":
	test = Instruction()

