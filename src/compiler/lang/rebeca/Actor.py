#!/usr/bin/python
# Filename: Actor.py
# Description: Implementation of the Actor class

from compiler.lang.rebeca.ReactiveClass import ReactiveClass
from compiler.lang.rebeca.RuntimeContext import RuntimeContext as RebecaRuntimeContext
from compiler.lang.program.RuntimeContext import RuntimeContext

from queue import PriorityQueue
import datetime

class Actor:
	def __init__(self, ctxt:RebecaRuntimeContext, rc:ReactiveClass, name:str, idents:list=None, params:list=None):
		self.name		= name		# Instance name
		self.rc			= rc		# Class type information
		self.ready		= False		# Runnable state
		self.ctxt		= None		# Runtime context
		self.created	= False		# Created state
		self.idents		= idents	# Known rebecs identifiers
		self.kr			= {}		# Known rebecs mapping
		self.params		= params	# Constructor parameters
		self.vars		= {}		# State variables
		self.mq			= PriorityQueue() 	# Message queue
		
		self.__build_vars(ctxt, rc)		
		return

	def __build_vars(self, ctxt:RebecaRuntimeContext, rc:ReactiveClass):
		for k, v in rc.state_vars.items():
			if v in ['string', 'boolean', 'int', 'float', 'double', 'byte']:
				self.vars[k] = None
				continue
			obj = ctxt.create_object(v)
			if obj is None:
				raise RuntimeError(f'Unsupported type [{v}] for state variable [{k}].')
			
			self.vars[k] = obj
		
		return
	

	def push_msg(self, msg):
		startat = datetime.datetime.now()  # Default priority
		delay	= msg[3]
		if delay is not None:
			startat += datetime.timedelta(milliseconds=delay)

		self.mq.put( (startat, msg) )
		return self
	
	def pop_msg(self):
		if not self.mq:
			return None
		
		# Peek at the next message without removing it
		nextitem = self.mq.queue[0]
		now		= datetime.datetime.now()

		# Check if the next message is ready to be processed
		if nextitem[0] > now:
			return None
		
		# Dequeue the next message
		item	= self.mq.get() 
		return item[1]

	@property
	def msgcount(self):
		return self.mq.qsize()

	@property
	def runnable(self):
		return self.ready
	
	
	def stop(self):
		self.ready = False
		return

	def construct(self, ctxt:RebecaRuntimeContext):
		if self.created == True:
			return self
		
		# Initialize known rebecs
		for n, var in enumerate(self.idents):

			# Identify the known rebec with its matching index
			kr		= self.rc.known_rebecs[n]

			# Get the instance with the matching name
			inst	= ctxt.get( var )
			if inst is None:
				raise RuntimeError(f'Unresolved reference variable [{var}] mapping rebec [{kr[0]}].')

			# Map the state variable to the known rebec instance
			self.kr[kr[0]] =inst

		# Call the constructor to initialize the instance
		self.__contructor( ctxt )

		self.created 	= True
		self.ready 		= True
		return self
	
	def destroy(self, ctxt):
		if self.rc.dtor:
			self.rc.dtor.run(self.ctxt)
		return
		
	def step(self, ctxt:RuntimeContext):
		if self.created == False: 	# Support lazy construction
			# Initialize and bind known rebecs from the global context
			self.construct(ctxt)
		
		if self.ready == False:
			return

		# Get the number of pending messages
		# IMPORTANT: Store the message count to avoid infinite loops
		# if new messages are added while processing the queue	
		num_msgs = self.msgcount
		
		# Process pending messages
		for n in range(num_msgs):
			msg = self.pop_msg()
			if msg is None:
				break

			# Unpack the message
			(ctxt, method, args, delay) = msg

			# Invoke the method
			self.__invoke( ctxt, method, args )

		return
	
	def invoke(self, ctxt:RuntimeContext, method:str, args, delay=None):
		return self.push_msg( (ctxt.fork(), method, args, delay) )

	def __invoke(self, ctxt:RuntimeContext, method:str, args):
		# Push a new stack frame
		ctxt.push( f'{self.name}.{method}' )

		# Set 'self' in the local context
		ctxt.set_self( self )

		# Invoke the function
		ret = self.rc.invoke(ctxt, method, args)

		# Pop the stack frame
		ctxt.pop()

		# Set the return value in the accumulator
		ctxt.ax = ret
		return ret

	def __contructor(self, ctxt:RebecaRuntimeContext):
		self.ctxt 		= ctxt.clone()

		# Set the 'self' pointer in the local context
		self.ctxt.set_self( self )

		if self.rc.ctor:
			# Run the constructor
			self.rc.ctor.run(self.ctxt, self.params)

		return self


if __name__ == "__main__":
	test = Actor()

