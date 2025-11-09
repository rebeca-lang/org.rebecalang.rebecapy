#!/usr/bin/python
# Filename: Port.py
# Description: Implementation of the Port class

from compiler.lang.program.RuntimeObject import RuntimeObject
from abc import ABC, abstractmethod

class Interface(ABC):
	@abstractmethod
	def send(self, fd, msg, options=None):
		""" Sends a message on a socket
		Arguments
			fd -- Socket handle
			msg -- Message to send
			options -- Message options
		"""
		pass

	@abstractmethod
	def receive(self, fd, options=None):
		""" Receives a message on a socket
		Arguments
			fd -- Socket handle
			options -- Message options
		"""
		pass

	@abstractmethod
	def is_pending(self, fd):
		""" Checks if there are pending messages
		Arguments
			fd -- Socket handle
		"""
		return False

	@abstractmethod
	def is_open(self, fd):
		""" Checks if the socket is open
		Arguments
			fd -- Socket handle
		"""
		return False

	@abstractmethod
	def setopt(self, fd, option, value):
		""" Sets option on the socket
		Arguments
			fd -- Socket handle
			option -- Option name
			value -- Option value
		"""
		return False

	@abstractmethod
	def getopt(self, fd, option):
		""" Returns current options on the socket
		Arguments
			fd -- Socket handle
			option -- Option name
		"""
		return False
	
	@abstractmethod
	def connect(self, fd, address:str):
		""" Connects the socket to an address
		Arguments
			fd -- Socket handle
			address -- Address to connect to
		"""
		return False

	@abstractmethod
	def open(self, fd, type:str):
		""" Opens the socekt
		Arguments
			fd -- Socket handle
			type -- Type of the socket
		"""
		return False

	@abstractmethod
	def close(self, fd):
		""" Closes the socket
		Arguments
			fd -- Socket handle
		"""
		return False

class Port(RuntimeObject):
	def __init__(self, ifc=None):
		""" Constructor
		Arguments
			ifc -- Interface for the socket driver
		"""
		RuntimeObject.__init__(self)
		self.ifc 	= ifc
		self.fd 	= None
		return

	@staticmethod
	def vtble(self):
		""" Returns the v-table
		"""
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
		""" Invokes a method on the list
		Arguments
			ctxt -- Runtime memory context
			method -- Method name
			args -- arguments
		"""
		return RuntimeObject.dispatch(self, [Port.vtble(self)], method, args)


	def set_interfaces(self, interface):
		""" Sets the interface for the socket API
		Arguments
			interface -- Interface for the socket driver
		"""
		self.interface = interface
		return self

	def is_open(self):
		""" Checks if the socket is open
		"""
		return self.interface is not None
	
	def open(self, type:str):
		""" Opens the socket
		Arguments
			type -- Type of the socket
		"""
		self.fd = self.interface.open(type)
		return self

	def close(self):
		""" Closes the socket
		"""
		self.interface.close(self.fd)
		self.ifc = None
		return self

	def connect(self, address:str):
		""" Connects the socket to an address
		Arguments
			address -- Address of the socket
		"""
		self.interface.connect(self.fd, address)
		return self
	
	def send(self, msg, options=None):
		""" Sends a message
		Arguments
			msg -- Message to send
			options -- Message options
		"""
		self.interface.send(self.fd, msg, options)
		return self
	
	def receive(self, options=None):
		""" Receives a message
		Arguments
			options -- Message options
		"""
		return self.interface.receive(self.fd, options)

	def is_pending(self):
		""" Checks if there are pending messages
		"""
		return self.interface.is_pending(self.fd)

	def setopt(self, option, value):
		""" Sets an option on the socket
		Arguments
			option -- Option name
			value -- Option value
		"""
		return self.interface.setopt(self.fd, option, value)

	def getopt(self, option):
		""" Gets an option on the socket
		Arguments
			option -- Option name
		"""
		return self.interface.getopt(self.fd, option)

	@property
	def interface(self):
		""" Returns the interface for the socket
		"""
		if self.ifc is None:
			raise RuntimeError('No interface defined for this port.')
		return self.ifc
	
	
if __name__ == "__main__":
	test = Port()

