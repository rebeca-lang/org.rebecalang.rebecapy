#!/usr/bin/python
# Filename: Program_test.py
# Description: Test cases for the Program class

from compiler.lang.program.Program import Program
from compiler.lang.program.RuntimeContext import RuntimeContext
from compiler.lang.program.Assignment import Assignment
from compiler.lang.program.If import If
from compiler.lang.program.For import For

import unittest

class ProgramTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		self.program = Program([
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
				)	])
		return
		
	def tearDown(self):
		return
		
	def test_print(self):
		print( f'------------\n{self.program}\n------------\n\n' )

	def test_run(self):
		context = RuntimeContext()
		self.program.run(context)
		print( context )

if __name__ == '__main__':
    unittest.main()
