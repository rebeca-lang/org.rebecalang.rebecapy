#!/usr/bin/python
# Filename: ReactiveClass_test.py
# Description: Test cases for the ReactiveClass class

from compiler.lang.rebeca.ReactiveClass import ReactiveClass
from compiler.lang.program.Instruction import Instructions
from compiler.lang.program.Program import Program
from compiler.lang.program.RuntimeContext import RuntimeContext
from compiler.lang.program.Assignment import Assignment
from compiler.lang.program.If import If
from compiler.lang.program.For import For

import unittest

class ReactiveClassTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):		
		p = [
			Assignment('count', '0'),
			Assignment('a', '0'),
			Assignment('b', '1'),
			Assignment('x', '5'),
			Assignment('x', '5'),
			Assignment('y', '10+20'),
			Assignment('y', 'x*y'),
			If ('x < y', [
				Assignment('z', 'x + y'),
				Assignment('z', 'x - y'),
					If ('a < b', [
						Assignment('a', 'x + y'),
						Assignment('b', 'x - y')]
						)
				]
				),
			For ([
				Assignment('count', 'count + 1')
				],
				'i', 0, 10, 5
				)		]
		
		rc = ReactiveClass('Train', 2)
		rc.know_rebec( 'BridgeController', 'bc')
		rc.state_var( 'byte', 'id')

		rc.constructor( {'byte':'id'}, [
			Assignment('count', '0'),
			]
		)
		rc.msg_server( 'reachBridge', p, {'byte':'id'})
		rc.msg_server( 'youMayPass')
		rc.msg_server( 'passed')
		self.rc = rc
		
	def tearDown(self):
		return
		
	def _test_print(self):
		print(self.rc)

	def test_call(self):
		self.rc.invoke(None, 'reachBridge', {'id':1})
		return
	
if __name__ == '__main__':
    unittest.main()
