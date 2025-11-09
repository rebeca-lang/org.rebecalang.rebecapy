#!/usr/bin/python
# Filename: Program.py
# Description: Implementation of the Program class

from compiler.lang.program.Instruction import Instructions
from compiler.lang.program.RuntimeContext import RuntimeContext

class Program:
	def __init__(self, name:str, instructions:Instructions=None, arglist=None):
		""" Constructor
		Arguments
			name -- Name of the program
			instructions -- Program instructions
			arglist -- Map of argument inputs
		"""
		assert instructions is None or isinstance(instructions, Instructions)
		self.trace			= False	# Trace flag		
		self.name			= name
		self.arglist		= arglist if arglist else {}
		self.instructions	= instructions if instructions else Instructions()
		return
		
	def append(self, instruction):
		""" Appends an instruction
		Arguments
			instruction -- Instruction to append
		"""
		self.instructions.append(instruction)
		return self
	
	def run(self, ctxt:RuntimeContext=None, args=None):
		""" Runs the program
		Arguments
			ctxt -- Runtime context memory 
			args -- Arguments to pass to the program
		"""
		if self.trace:
			ctxt.trace(f'{self.name}( {args} )')

		if args is not None:
			if len(args) != len(self.arglist):
				raise RuntimeError(f'{self.name}: Argument count mismatch. Expected {len(self.arglist)}, got {len(args)}.')
 
			if isinstance(args, list):
				args = {self.arglist[i][1]: args[i] for i in range(len(args))}

		if self.trace:
			print(ctxt)
			
		# Invoke the method with the given arguments
		self.instructions.execute(ctxt, self.name, args)
		return None
	
	def invoke(self, selfInst, ctxt:RuntimeContext=None, args=None):
		""" Invokes the method
		Arguments
			selfInst -- Reference to the an object instance
			ctxt -- Runtime memory context
			args -- Arguments to pass to the program
		"""
		return self.run(ctxt, args)

	def __str__(self):
		""" A string notation of the object
		"""
		args = []
		for a in self.arglist:
			args.append(f'{a[0]} {a[1]}')

		return f'({','.join(args)}){{\n{str(self.instructions)}\n}}\n'
		

if __name__ == "__main__":
	test = Program()

