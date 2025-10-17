#!/usr/bin/python
# Filename: List.py
# Description: Implementation of the List class

from compiler.lang.objects.Containers import Container
from compiler.lang.program.RuntimeObject import RuntimeObject

class List(Container, list):
	def __init__(self, maxsize=-1):
		list.__init__(self)
		Container.__init__(self, maxsize)
		return

	@staticmethod
	def vtble(self):
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
		return RuntimeObject.dispatch(self, [List.vtble(self)], method, args)

	def add(self, item):
		self.check_full(len(self))
		self.append(item)
		return self
	
	def remove(self, item):	
		if item in self:
			super().remove(item)
		return self
	
	def clear(self):
		return super().clear()
	
	def count(self):
		return len(self)
	
	def contains(self, item):
		return item in self
	
	def index(self, item):
		if item in self:
			return super().index(item)
		return -1

	def at(self, index:int):
		return super().__getitem__(index)

	def setat(self, index:int, value):
		return super().__setitem__(index, value)

	def insert(self, index, item):
		self.check_full(len(self))
		super().insert(index, item)
		return self
	
	def tostring(self, sep=', '):
		return sep.join( [ str(i) for i in self ] )
	
	def fromstring(self, s:str, sep=','):
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
