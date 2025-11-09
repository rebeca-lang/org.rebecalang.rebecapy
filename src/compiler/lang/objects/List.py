#!/usr/bin/python
# Filename: List.py
# Description: Implementation of the List class

from compiler.lang.objects.Containers import Container
from compiler.lang.program.RuntimeObject import RuntimeObject

class List(Container, list):
	def __init__(self, maxsize=-1):
		""" Constructor
		Arguments
			maxsize -- Maximum size of the container
		"""
		list.__init__(self)
		Container.__init__(self, maxsize)
		return

	@staticmethod
	def vtble(self):
		""" Returns the v-table
		"""
		return {
			'add':		self.add,
			'remove':	self.remove,
			'at':		self.at,
			'setat':	self.setat,
			'clear':	self.clear,
			'count':	self.count,
			'contains':	self.contains,
			'index':	self.index,
			'insert':	self.insert,
			'tostring':	self.tostring,
			'fromstring':self.fromstring
		}
	
	def invoke(self, ctxt, method:str, args):
		""" Invokes a method on the list
		Arguments
			ctxt -- Runtime memory context
			method -- Method name
			args -- arguments
		"""
		return RuntimeObject.dispatch(self, [List.vtble(self)], method, args)

	def add(self, item):
		""" Adds an item to the list
		Arguments
			item -- Item to add
		"""
		self.check_full(len(self))
		self.append(item)
		return self
	
	def remove(self, item):	
		""" Removes an item from the list
		Arguments
			item -- Item to remove
		"""
		if item in self:
			super().remove(item)
		return self
	
	def clear(self):
		""" Clears the list
		"""
		return super().clear()
	
	def count(self):
		""" Returns the items in the list
		"""
		return len(self)
	
	def contains(self, item):
		""" Checks if an item is in the list
		Arguments
			item -- Item to search for
		"""
		return item in self
	
	def index(self, item):
		""" Returns the indes of the item in the list
		Arguments
			item -- Index of the item in the list
		"""
		if item in self:
			return super().index(item)
		return -1

	def at(self, index:int):
		""" Returns an item at an index
		Arguments
			index -- Index of the item in the list
		"""
		return super().__getitem__(index)

	def setat(self, index:int, item):
		""" Sets an item value at an index
		Arguments
			index -- Index of the item in the list
			item -- Item to set
		"""
		return super().__setitem__(index, item)

	def insert(self, index, item):
		""" Inserts an item at an index
		Arguments
			index -- Index of the item in the list
			item -- Item to set
		"""
		self.check_full(len(self))
		super().insert(index, item)
		return self
	
	def tostring(self, sep=', '):
		""" Returns a string notation of the list
		Arguments
			sep -- Separator
		"""
		return sep.join( [ str(i) for i in self ] )
	
	def fromstring(self, s:str, sep=','):
		""" Creates the list from the string
		Arguments
			s -- String to decode
			sep -- Separator
		"""
		self.clear()
		for item in s.split(sep):
			self.append( item.strip() )
		return self

		

if __name__ == "__main__":
	test = List()

	test.add('task1')
	test.add('task2')

	print (test.count())
	print(test.tostring())
	print(test.remove('task2'))
	print(test.tostring())
	print(test.count())
