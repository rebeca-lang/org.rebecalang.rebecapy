#!/usr/bin/python
# Filename: Port.py
# Description: Implementation of the Port class

from compiler.lang.program.RuntimeObject import RuntimeObject
from abc import ABC, abstractmethod

class Interface(ABC):
	@abstractmethod
	def send(self, fd, msg, options=None):
		pass

	@abstractmethod
	def receive(self, fd, options=None):
		pass

	@abstractmethod
	def is_pending(self, fd):
		return False

	@abstractmethod
	def is_open(self, fd):
		return False

	@abstractmethod
	def setopt(self, fd, option, value):
		return False

	@abstractmethod
	def getopt(self, fd, option):
		return False
	
	@abstractmethod
	def connect(self, fd, address:str):
		return False

	@abstractmethod
	def open(self, fd, type:str):
		return False

	@abstractmethod
	def close(self, fd):
		return False

class Port(RuntimeObject):
	def __init__(self, ifc=None):
		RuntimeObject.__init__(self)
		self.ifc 	= ifc
		self.fd 	= None
		return

	@staticmethod
	def vtble(self):
		return {
			'open': self.open,
			'connect': self.connect,
			'close': self.close,
			'send': self.send,
			'receive': self.receive,
			'pending': self.is_pending,
			'setopt': self.setopt,
			'getopt': self.getopt
		}
	
	def invoke(self, ctxt, method:str, args):
		return RuntimeObject.dispatch(self, [Port.vtble(self)], method, args)


	def set_interfaces(self, interface):
		self.interface = interface
		return self

	def is_open(self):
		return self.interface is not None
	
	def open(self, type:str):
		self.fd = self.interface.open(type)
		return self

	def close(self):
		self.interface.close(self.fd)
		self.ifc = None
		return self

	def connect(self, address:str):
		self.interface.connect(self.fd, address)
		return self
	
	def send(self, msg, options=None):
		self.interface.send(self.fd, msg, options)
		return self
	
	def receive(self, options=None):
		return self.interface.receive(self.fd, options)

	def is_pending(self):
		return self.interface.is_pending(self.fd)

	def setopt(self, option, value):
		return self.interface.setopt(self.fd, option, value)

	def getopt(self, option):
		return self.interface.getopt(self.fd, option)

	@property
	def interface(self):
		if self.ifc is None:
			raise RuntimeError('No interface defined for this port.')
		return self.ifc
	
	
if __name__ == "__main__":
	test = Port()

