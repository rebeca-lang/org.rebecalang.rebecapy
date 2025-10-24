#!/usr/bin/python
# Filename: Module.py
# Description: Implementation of the Module class

from compiler.lang.rebeca.ReactiveClass import ReactiveClass
from compiler.lang.rebeca.Main import Main
from compiler.lang.rebeca.RuntimeContext import RuntimeContext as RebecaRuntimeContext
from compiler.lang.rebeca.Factory import Factory
from compiler.lang.program.Assignment import Assignment 

class Module:
	def __init__(self, classes:list=None, main:Main=None):
		self.envs	    = []
		self.classes 	= classes if classes else []
		self.main 		= main if main is not None else Main()
		return

	def add_env(self, value):
		self.envs.append((value))
		return
	
	def get(self, name:str):
		for c in self.classes:
			if c.name == name:
				return c
		return None
	
	def reactive_class(self, name:str, queue_size:int=-1):
		rclass 			= ReactiveClass(name, queue_size)
		self.classes.append(rclass)
		return rclass
	
	def create(self, interfaces:dict=None, argv:dict=None):
		ctxt	= RebecaRuntimeContext(self, Factory(interfaces))
		ctxt.create(self, argv)
		return ctxt


	def __str__(self):
		lines = []

		for c in self.classes:
			lines.append(str(c))

		if self.main:
			lines.append(str(self.main))
			
		return '\n'.join(lines)

if __name__ == "__main__":
	test = Module()

