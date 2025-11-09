#!/usr/bin/python
# Filename: StateMachine.py
# Description: Implementation of the StateMachine class

from compiler.lang.program.RuntimeObject import RuntimeObject
import json

class StateMachine(RuntimeObject):
	def __init__(self):
		""" Constructor
		"""
		RuntimeObject.__init__(self)
		self._states = {}
		self._current = None
		self._default = None
		return

	@staticmethod
	def vtble(self):
		""" Virtual table of the StateMachine class
		"""
		return {
			'transition':	self.transition,
			'add':			self.add,
			'remove':		self.remove,
			'current':		self.current,
			'set_current':	self.set_current,
			'default':		self.default,
			'set_default':	self.set_default,
			'has':			self.has,
			'load':			self.load,
			'save':			self.save,
			'reset':		self.reset
		}
	
	def invoke(self, ctxt, method:str, args):
		""" Invokes a method on the state machine
		Arguments
			ctxt -- Runtime memory context
			method -- Method name
			args -- arguments
		"""
		return RuntimeObject.dispatch(self, [StateMachine.vtble(self),StateMachine.vtble(self)], method, args)

	def transition(self, state_input):
		""" Transitions the state machine to a new state
		Arguments
			state_input -- Input that triggers the transition
		"""
		state	= self._states.get(self._current, None)

		if state is None:
			return

		new_state = state.get(state_input, None)
		if new_state is not None:
			self._current = new_state

		return

	def add(self, current, input, state_to):
		""" Adds a state transition
		Arguments
			current -- Current state
			input -- Input to trigger the transition
			state_to -- Target state
		"""
		if current not in self._states:
			self._states[current] = {input:state_to}
		else:
			self._states[current][input] = state_to
		return

	def remove(self, current, input):
		""" Removes a state transition
		Arguments
			current -- Current state
			input -- Input to trigger the transition
		"""
		state	= self._states.get(current, None)
		if state is None:
			return
		
		state.pop(input, None)
		return
	
	def current(self):
		""" Returns the current state
		"""
		return self._current
	
	def set_current(self, state):
		""" Sets the current state
		Arguments
			state -- New current state
		"""
		self._current = state
		return

	def default(self):
		""" Returns the default state
		"""
		return self._default
	
	def set_default(self, state):
		""" Sets the default state
		Arguments
			state -- New default state
		"""
		self._default = state
		return

	def has(self, current, input):
		""" Checks if a state transition exists
		Arguments
			current -- Current state
			input -- Input to trigger the transition
		"""
		state	= self._states.get(current, None)
		if state is None:
			return False
		
		return True if input in state else False
	
	def load(self, path):
		""" Loads the state machine from a file
		Arguments
			path -- Path to the JSON file
		"""
		json_data 		= json.load(open(path, 'r'))
		self._default	= json_data.get('default', None)
		self._states 	= json_data.get('states', {})
		self._current 	= self._default
		return

	def save(self, path):
		""" Saves the state machine to a file
		Arguments
			path -- Path to the JSON file
		"""
		json.dump({
			'default': self._default,
			'states': self._states
		}, open(path, 'w'), indent=4)

	def reset(self):
		""" Resets the state machine to the default state
		"""
		self._current = self._default
		return
	

	def __str__(self):
		""" A string notation of the object
		"""
		return f"StateMachine(states={self._states})"
	
if __name__ == "__main__":
	sample = StateMachine()
	sample.add('A', 'to.B', 'B')
	sample.add('A', 'to.C', 'C')
	sample.add('B', 'to.A', 'A')
	sample.add('B', 'to.A', 'D')
	sample.add('B', 'to.C', 'C')
	sample.add('C', 'to.A', 'A')

	sample.save('statemachine.json')

	test = StateMachine()
	test.load('statemachine.json')
	test.set_current('A')

	print(test.current())
	test.transition('to.B')
	print(test.current())
	test.transition('to.C')
	print(test.current())
	test.transition('to.A')
	print(test.current())


