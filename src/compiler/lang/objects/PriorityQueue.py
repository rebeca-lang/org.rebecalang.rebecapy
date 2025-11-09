#!/usr/bin/python
# Filename: PriorityQueue.py
# Description: Implementation of the PriorityQueue class

from compiler.lang.objects.Containers import Container
from compiler.lang.objects.List import List
from compiler.lang.program.RuntimeObject import RuntimeObject
import heapq

class PriorityQueue(List):
	def __init__(self, maxsize=-1):
		""" Constructor
		Arguments
			maxsize -- Maximum size of the container
		"""
		List.__init__(self, maxsize)
		return
        
	@staticmethod
	def vtble(self):
		""" Returns the v-table
		"""
		return {
			'push':		self.push,
			'pop':		self.pop
		}
	
	def invoke(self, ctxt, method:str, args):
		""" Invokes a method on the priority queue
		Arguments
			ctxt -- Runtime memory context
			method -- Method name
			args -- arguments
		"""
		return RuntimeObject.dispatch(self, [PriorityQueue.vtble(self),List.vtble(self)], method, args)

	def push(self, priority, item):
		""" Pushes an item onto the priority queue
		Arguments
			priority -- Priority of the item
			item -- Item to push
		"""
		self.check_full(len(self))
		heapq.heappush(self, (priority, item))
		return self
	
	def pop(self):	
		""" Pops the highest priority item from the priority queue
		"""
		if len(self) == 0:
			return None

		priority, item	= heapq.heappop(self) 
		return item
	
			
	def tostring(self, sep=', '):
		""" Returns a string representation of the priority queue
		Arguments
			sep -- Value separator
		"""
		return sep.join( [ f'{i[0]}={str(i[1])}' for i in self ] )
	
	def fromstring(self, s:str, sep=','):
		""" Constructs a priority queue from a string representation
		Arguments
			sep -- Value separator
		"""
		self.clear()
		for item in s.split(sep):
			heapq.heappush(self, item.strip().split('='))
		return self
		

if __name__ == "__main__":
	test = PriorityQueue()
	print (test.count())
	test.push(5, 'task1')
	test.push(1, 'task2')

	print (test.count())
	print(test.tostring())
	print(test.pop())
	print(test.tostring())
	print(test.pop())
	print(test.tostring())
	print(test.pop())
	print (test.count())

