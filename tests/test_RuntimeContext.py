#!/usr/bin/python
# Filename: RuntimeContext_test.py
# Description: Test cases for the RuntimeContext class

from compiler.lang.program.RuntimeContext import RuntimeContext

import unittest

class RuntimeContextTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		self.context = RuntimeContext()
		return
		
	def tearDown(self):
		return

	def test_split(self):
		context = RuntimeContext()
		self.assertEqual( str(context.ip), 'global:1' )
		context.next()
		self.assertEqual( str(context.ip), 'global:2' )
		context.goto(5)
		self.assertEqual( str(context.ip), 'global:5' )
		context.push('Rebec1.msg1', 1)
		self.assertEqual( str(context.ip), 'Rebec1.msg1:1' )
		context.pop()
		self.assertEqual( str(context.ip), 'global:5' )



if __name__ == '__main__':
    unittest.main()
