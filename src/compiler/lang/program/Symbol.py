#!/usr/bin/python
# Filename: Symbol.py
# Description: Implementation of the Symbol class

class Symbol:
	def __init__(self, name:str):
		""" Constructor
		Arguments
			name -- Symbol name
		"""
		self.name	= name
		return

	def __str__(self):
		""" A string notation of the object
		"""
		return self.name
		

if __name__ == "__main__":
	test = Symbol()

