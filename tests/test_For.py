#!/usr/bin/python
# Filename: ForBlock_test.py
# Description: Test cases for the ForBlock class

from compiler.lang.program.RuntimeContext import RuntimeContext
from compiler.lang.program.Assignment import Assignment
from compiler.lang.program.For import For
import unittest

class ForBlockTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		self.stmt = For ([
				Assignment('count', 'count + 1')
				],
				'i', 0, 10, 5
				)

		return
		
	def tearDown(self):
		return
		
	def test_print(self):
		print( self.stmt )
		return

	def test_instruction(self):
		context = RuntimeContext()
		context.set('count', 0)
		self.stmt.execute(context)

		self.assertEqual(context.get('count'), 2)

if __name__ == '__main__':
    unittest.main()
