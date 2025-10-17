#!/usr/bin/python
# Filename: Map.py
# Description: Implementation of the Map class

from compiler.lang.objects.Containers import Container
from compiler.lang.program.RuntimeObject import RuntimeObject

class Map(Container, dict):
	def __init__(self, maxsize=-1):
		dict.__init__(self)
		Container.__init__(self, maxsize)
		return

	def vtble(self):
		return {
			'set':		self.set,
			'get':		self.get,
			'has':		self.has,
			'remove':	self.remove,
			'clear':	self.clear,
			'count':	self.count,
			'tostring':	self.tostring,
			'fromstring':self.fromstring
		}

	
	def invoke(self, ctxt, method:str, args):
		return RuntimeObject.dispatch(self, [Map.vtble(self)], method, args)

	def set(self, name, value):
		self.check_full(len(self))
		return self.__setitem__(name, value)

	def get(self, name):
		return self.__getitem__(name)
	
	def has(self, name):
		return name in self
	
	def remove(self, name):
		if name in self:
			del self[name]
		return self
	
	def clear(self):	
		return super().clear()
	
	def count(self):
		return len(self)
	
	def tostring(self, sep=','):
		return sep.join( [ f'{k}:{v}' for k,v in self.items() ] )
	
	def fromstring(self, s:str, sep=',='):	
		self.clear()
		for item in s.split(se[0]):
			kv = item.split(sep[1])
			if len(kv) != 2:
				raise RuntimeError(f'Invalid map entry: {item}')
			self[kv[0].strip()] = kv[1].strip()
		return self

		

if __name__ == "__main__":
	test = Map()

	test.set('jack', 4098)
	test.set('sape', 4139)
	test.set('guido', 4127)


	print( test.tostring() )
	print( test.get('jack') )

