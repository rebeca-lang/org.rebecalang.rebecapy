#!/usr/bin/python
# Filename: VirtualMachine.py
# Description: Implementation of the VirtualMachine class

from matplotlib import lines
from compiler.lang.rebeca.Parser import Parser
from compiler.lang.rebeca.Module import Module
from compiler.lang.rebeca.PreProcessor import PreProcessor

class VirtualMachine:
	def __init__(self):
		self.parser  = Parser()
		self.trace   = False
		return

	@property
	def module(self):
		return self.parser.module

	def load(self, file):
		# Build the parser
		self.parser.build()
				
		# Preprocess the file to resolve imports
		lines 		= PreProcessor().process(file)
		text		= '\n'.join(lines)

		if self.trace:
			for n, l in enumerate(lines):
				print(f'{n}: {l}')

		# Parse the preprocessed file
		self.parser.parse( text, file )
		return
	

	def start(self):
		self.ctxt	= self.module.create()
		return

	def run(self):
		# Step through the context if it is runnable
		while self.ctxt.runnable:
			self.ctxt.step()
		return		

	def step(self):
		# Step through the context if it is runnable
		if self.ctxt.runnable:
			self.ctxt.step()
			return True
		
		return False

	def stop(self):
		self.ctxt.destroy()
		return

if __name__ == "__main__":
	test = VirtualMachine()

