#!/usr/bin/python
# Filename: Symbol.py
# Description: Implementation of the Symbol class

class Symbol:
	def __init__(self, name:str):
		self.name	= name
		return

	def __str__(self):
		return self.name
		

if __name__ == "__main__":
	test = Symbol()

