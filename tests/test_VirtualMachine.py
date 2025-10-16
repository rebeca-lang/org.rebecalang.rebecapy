#!/usr/bin/python
# Filename: VirtualMachine_test.py
# Description: Test cases for the VirtualMachine class

from compiler.lang.rebeca.VirtualMachine import VirtualMachine

import unittest

class VirtualMachineTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_test(self):
		vm = VirtualMachine()
		vm.load('samples\\basics\\helloworld.rebeca')
		vm.start()

		for i in range(100):
			vm.step()

		vm.stop()
		self.assertTrue(True)
		return

if __name__ == '__main__':
    unittest.main()
