#!/usr/bin/python
# Filename: Rebeca.py
# Description: Implementation of the singleton Rebeca application

from compiler.lang.rebeca.VirtualMachine import VirtualMachine
import os

class Rebeca:
	def __init__(self):
		self.steps	= 1000
		return

	def run(self, args, appinfo):		
		self.configure(args, appinfo)
		self.simulate( args[-1])
		return -1
		
	def configure(self, args, appinfo):
		if len(args) == 0:
			return
		
		for help in appinfo["help"]:
			if help[0] != args[0]:
				continue

			method = args[0]
			if hasattr(self, method) and callable(func:=getattr(self, method)):
				try:
					args 	= args[1:]
					if len(args) == 0:
						args	= None

					result	= func( args )				
				except Exception as e:
					print(e)
					return -1
				
		return 0
		
	def step(self, args):
		self.steps	= int(args[0])
		return 0
	
	def simulate(self, file):
		try:
			if os.path.isfile(file) == False:
				print("Error: File not found - {}".format(file))
				return -1
					
			vm = VirtualMachine()
			vm.load(file)
			vm.start()

			for i in range(self.steps):
				vm.step()

			vm.stop()
		except Exception as e:
			print(e)
		return

if __name__ == "__main__":
    test = Rebeca()

