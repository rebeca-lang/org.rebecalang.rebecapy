#!/usr/bin/python
# Filename: IfBlock_test.py
# Description: Test cases for the IfBlock class

from compiler.lang.program.RuntimeContext import RuntimeContext
from compiler.lang.program.If import If
from compiler.lang.program.Assignment import Assignment
import unittest

class IfBlockTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		self.stmt =	If ('x < y', [
				Assignment('z', 'x + y'),
				])
		return
		
	def tearDown(self):
		return

	def test_print(self):
		print( self.stmt )
		return

	def test_instruction(self):
		context = RuntimeContext()
		context.set('x', 5)
		context.set('y', 10)
		self.stmt.execute(context)

		self.assertEqual(context.get('z'), 15)

if __name__ == '__main__':
    unittest.main()
