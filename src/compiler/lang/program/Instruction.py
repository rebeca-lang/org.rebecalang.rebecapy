#!/usr/bin/python
# Filename: Instruction.py
# Description: Implementation of the Instruction class

from compiler.lang.program.RuntimeContext import RuntimeContext
from abc import ABC, abstractmethod

# Base class for all instructions
class Instruction(ABC):
	def __init__(self, statements=None):
		""" Constructor
		Arguments
			statements -- #TODO
		"""
		self.ip			= 0	
		return
	
	def reset(self):
		""" #TODO
		"""
		self.ip	= 0
		return self
	
	def location(self, context):
		""" #TODO
		Arguments
			context -- #TODO
		"""
		self.module		= context[0]
		self.line		= context[1]
		return self

	def throw(self, msg):
		""" #TODO
		Arguments
			msg -- #TODO
		"""
		raise RuntimeError(f'Runtime error at {self.module}({self.line}) : {msg}')
	
	@abstractmethod
	def execute(self, runtime, ctxt, frame):
		""" Execute the instruction
		Arguments
			runtime -- Runtime environment
			ctxt -- Runtime memory context
			frame -- Call stack frame
		"""
		pass

	@staticmethod
	def argstostring(args):
		""" Convert arguments to string representation
		Arguments
			args -- arguments
		"""
		arglist	= []
		for a in args:
			arglist.append(str(a))
		return arglist


# Subclass representing a block of instructions
class Instructions(Instruction):
	def __init__(self, instructions=None):
		""" Constructor
		Arguments
			instructions -- Instructions to execute within the block
		"""
		Instruction.__init__(self)
		self.instructions	= instructions if instructions is not None else []
		return

	def append(self, instruction):
		""" Append an instruction to the block
		Arguments
			instruction -- Instruction to append
		"""
		self.instructions.append(instruction)
		return

	def execute(self, ctxt:RuntimeContext, scope:str, args=None):
		""" Execute the block of instructions
		Arguments
			ctxt -- Runtime memory context
			scope -- Current variable scope
			args -- Arguments to pass to the instructions
		"""
		# Add the function name and arguments to the context stack
		ctxt.push(scope, args)
		for i in self.instructions:
			i.execute(ctxt)

		# Pop the stack frame
		ctxt.pop()
		return None

	def __str__(self):
		""" A string notation of the object
		"""
		lines = [str(i) for i in self.instructions]
		return '\n'.join(lines)

if __name__ == "__main__":
	test = Instruction()

