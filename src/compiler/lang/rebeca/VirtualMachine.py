#!/usr/bin/python
# Filename: VirtualMachine.py
# Description: Implementation of the VirtualMachine class

from compiler.lang.rebeca.Parser import Parser
from compiler.lang.rebeca.Module import Module
from compiler.lang.rebeca.PreProcessor import PreProcessor

class VirtualMachine:
	def __init__(self, interfaces:dict= None):
		""" Constructor
		Arguments
			interfaces -- Interface definitions
		"""
		self.parser  = Parser()
		self.trace   = False
		self.ifc	 = interfaces
		self.ctxt    = None
		return

	@property
	def module(self):
		""" Returns the modue of the parser.
		"""
		return self.parser.module

	def load(self, file):
		""" Loads and parses a Rebeca source file.
		Arguments
			file -- Path to the Rebeca source file
		"""
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
		""" Starts the virtual machine with the given arguments.
		Arguments
			argv -- Command line arguments
		"""
		self.ctxt	= self.module.create(self.ifc, argv)
		return

	def run(self):
		""" Runs the virtual machine until completion.
		"""
		# Step through the context if it is runnable
		while self.ctxt.runnable:
			self.ctxt.step()
		return		

	def step(self, numsteps=1):
		""" Runs the virtual machine for a number of steps.
		Arguments
			numsteps -- Number of steps to execute
		"""
		# Step through the context if it is runnable
		for i in range(numsteps):
			self.ctxt.step()

		return True
		

	def stop(self):
		""" Stops the virtual machine.
		"""
		self.ctxt.destroy()
		return
	
	def pending(self):
		""" Checks if the virtual machine is pending execution.
		"""
		return self.ctxt.pending

	def invoke(self, var:str, method:str, args):
		""" Invokes a method on a variable with the given arguments.
		Arguments
			var -- Variable name
			method -- Method name
			args -- arguments
		"""
		obj = self.get_instance(var)

		if obj is None:
				raise Exception(f"Error: Object '{var}' not found.")
		
		return obj.push_msg( (self.ctxt.fork(), method, args) )

	def get_instance(self, name:str):
		""" Retrieves an instance by name.
		Arguments
			name -- Instance name
		"""
		return self.ctxt.instances.get(name, None)
	
if __name__ == "__main__":
	test = VirtualMachine()

