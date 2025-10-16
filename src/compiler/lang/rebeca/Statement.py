#!/usr/bin/python
# Filename: Statement.py
# Description: Implementation of the Statement class

from abc import ABC, abstractmethod

class Statement(ABC):
	def __init__(self):
		return
	
	@abstractmethod
	def execute(self, runtime, ctxt, frame):
		pass

		

if __name__ == "__main__":
	test = Statement()

