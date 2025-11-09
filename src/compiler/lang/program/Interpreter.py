#!/usr/bin/python
# Filename: Interpreter.py
# Description: Implementation of the Interpreter class

import compiler.lang.program.Program as Program
import compiler.lang.program.Expression as Expression
import compiler.lang.program.Instruction as Instruction
import compiler.lang.program.RuntimeContext as RuntimeContext

class Interpreter:
	def __init__(self):
		""" Constructor
		"""
		return

	def interpret(self, program):
		""" Interpret the given program
		Arguments
			program -- Program to interpret
		"""
		ctxt = RuntimeContext()
		return program.evaluate(ctxt)
		

if __name__ == "__main__":
	test = Interpreter()

