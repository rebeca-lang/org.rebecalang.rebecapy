#!/usr/bin/python
# Filename: Statement.py
# Description: Implementation of the Statement class

from abc import ABC, abstractmethod

class Statement(ABC):
	def __init__(self):
		""" Constructor
		"""
		return
	
	@abstractmethod
	def execute(self, runtime, ctxt, frame):
		""" Execute the statement in the given runtime context.
		Arguments
			runtime -- Runtime environment
			ctxt -- Runtime memory context
			frame -- Current stack frame
		"""
		pass

		

if __name__ == "__main__":
	test = Statement()

