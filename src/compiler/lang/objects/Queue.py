#!/usr/bin/python
# Filename: Queue.py
# Description: Implementation of the Queue class

from compiler.lang.objects.Containers import Container
from compiler.lang.objects.List import List
from compiler.lang.program.RuntimeObject import RuntimeObject

class Queue(List):
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
		""" Invokes a method on the queue
		Arguments
			ctxt -- Runtime memory context
			method -- Method name
			args -- arguments
		"""
		return RuntimeObject.dispatch(self, [Queue.vtble(self),List.vtble(self)], method, args)

	def push(self, item):
		""" Pushes an item onto the queue
		Arguments
			item -- Item to push
		"""
		self.check_full(len(self))
		self.append(item)
		return self
	
	def pop(self):	
		""" Pops an item from the front of the queue
		"""
		if len(self) == 0:
			return None
		return super().pop(0)
	

		

if __name__ == "__main__":
	test = Queue()

	test.push('task1')
	test.push('task2')

	print (test.count())
	print(test.tostring())
	print(test.pop())
	print(test.tostring())
	print(test.pop())
	print(test.tostring())
	print(test.pop())
	print(test.count())
