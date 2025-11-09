#!/usr/bin/python
# Filename: Map.py
# Description: Implementation of the Map class

from compiler.lang.objects.Containers import Container
from compiler.lang.program.RuntimeObject import RuntimeObject

class Map(Container, dict):
	def __init__(self, maxsize=-1):
		""" Constructor
		Arguments
			maxsize -- Maximum size of the container
		"""
		dict.__init__(self)
		Container.__init__(self, maxsize)
		return

	def vtble(self):
		""" Returns the v-table
		"""
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
		""" Invokes a method on the map
		Arguments
			ctxt -- Runtime memory context
			method -- Method name
			args -- arguments
		"""
		return RuntimeObject.dispatch(self, [Map.vtble(self)], method, args)

	def set(self, name, value):
		""" Sets an item with a key
		Arguments
			name -- Key name
			value -- Key value
		"""
		self.check_full(len(self))
		return self.__setitem__(name, value)

	def get(self, name):
		""" Returns an item with a key name
		Arguments
			name -- Key name
		"""
		if self.has(name) is False:
			return None
		return self.__getitem__(name)
	
	def has(self, name):
		""" Checks if the maps has a key value
		Arguments
			name -- Key name
		"""
		return name in self
	
	def remove(self, name):
		""" Removes a value with a key name
		Arguments
			name -- Key name
		"""
		if name in self:
			del self[name]
		return self
	
	def clear(self):	
		""" Clears the map
		"""
		return super().clear()
	
	def count(self):
		""" Returns the number of items in the map
		"""
		return len(self)
	
	def tostring(self, sep=','):
		""" Returns a string notation of the map
		Arguments
			sep -- Separator
		"""
		return sep.join( [ f'{k}:{v}' for k,v in self.items() ] )
	
	def fromstring(self, s:str, sep=',='):	
		""" Creates the map from the string
		Arguments
			s -- String to decode
			sep -- Separator
		"""
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

