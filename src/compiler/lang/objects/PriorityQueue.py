#!/usr/bin/python
# Filename: PriorityQueue.py
# Description: Implementation of the PriorityQueue class

from compiler.lang.objects.Containers import Container
from compiler.lang.objects.List import List
from compiler.lang.program.RuntimeObject import RuntimeObject
import heapq

class PriorityQueue(List):
	def __init__(self, maxsize=-1):
		List.__init__(self, maxsize)
		return
        
	@staticmethod
	def vtble(self):
		return {
			'push':		self.push,
			'pop':		self.pop
		}
	
	def invoke(self, ctxt, method:str, args):
		return RuntimeObject.dispatch(self, [Queue.vtble(self),List.vtble(self)], method, args)

	def push(self, priority, item):
		self.check_full(len(self))
		heapq.heappush(self, (priority, item))
		return self
	
	def pop(self):	
		if len(self) == 0:
			return None
		return heapq.heappop(self)
	
			
	def tostring(self, sep=', '):
		return sep.join( [ f'{i[0]}={str(i[1])}' for i in self ] )
	
	def fromstring(self, s:str, sep=','):
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

