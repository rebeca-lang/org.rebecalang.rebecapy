#!/usr/bin/python
# Filename: VirtualMachine.py
# Description: Implementation of the VirtualMachine class

from compiler.lang.rebeca.Parser import Parser
from compiler.lang.rebeca.Module import Module
from compiler.lang.rebeca.PreProcessor import PreProcessor

class VirtualMachine:
	def __init__(self, interfaces:dict= None):
		self.parser  = Parser()
		self.trace   = False
		self.ifc	 = interfaces
		self.ctxt    = None
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
	

	def start(self, argv:dict=None):
		self.ctxt	= self.module.create(self.ifc, argv)
		return

	def run(self):
		# Step through the context if it is runnable
		while self.ctxt.runnable:
			self.ctxt.step()
		return		

	def step(self, numsteps=1):
		# Step through the context if it is runnable
		for i in range(numsteps):
			if self.ctxt.runnable == False:
				return False
			self.ctxt.step()

		return True
		

	def stop(self):
		self.ctxt.destroy()
		return
	
	def runnable(self):
		return self.ctxt.runnable

	def invoke(self, var:str, method:str, args):
		obj = self.get_instance(var)

		if obj is None:
				raise Exception(f"Error: Object '{var}' not found.")
		
		return obj.push_msg( (self.ctxt.fork(), method, args) )

	def get_instance(self, name:str):
		return self.ctxt.instances.get(name, None)
	
if __name__ == "__main__":
	test = VirtualMachine()

