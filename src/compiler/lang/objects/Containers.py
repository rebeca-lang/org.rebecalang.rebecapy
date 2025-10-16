#!/usr/bin/python
# Filename: Container.py
# Description: Implementation of the Container class

from compiler.lang.program.RuntimeObject import RuntimeObject

class Container(RuntimeObject):
	def __init__(self, maxsize=0):
		RuntimeObject.__init__(self)
		self.maxsize = maxsize
		return
	
	def check_full(self, length):
		if self.maxsize > 0 and length >= self.maxsize:
			raise RuntimeError('Container is full')
			
	
if __name__ == "__main__":
	test = Container()

