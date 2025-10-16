#!/usr/bin/python
# Filename: Assignment_test.py
# Description: Test cases for the Assignment class

from compiler.lang.program.RuntimeContext import RuntimeContext
from compiler.lang.program.Assignment import Assignment
import unittest

class AssignmentTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		self.stmt = Assignment('a', '5 + 10')
		return
		
	def tearDown(self):
		return

	def test_print(self):
		print( self.stmt )
		return

	def test_instruction(self):
		context = RuntimeContext()
		self.stmt.execute(context)
		self.assertEqual(context.get('a'), 15)

if __name__ == '__main__':
    unittest.main()
