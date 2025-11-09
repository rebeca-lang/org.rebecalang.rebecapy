#!/usr/bin/python
# Filename: PreProcessor.py
# Description: Implementation of the rebeca preprocessor class

from compiler.lang.program.PreProcessor import PreProcessor as PreprocessorBase
import os

class PreProcessor(PreprocessorBase):
	def __init__(self, includes=None):
		""" Constructor
		Arguments
			includes -- List of include paths
		"""
		PreprocessorBase.__init__(self, includes)
		return

	def process_import(self, result, pathinfo, line):
		""" #TODO
		Arguments
			result -- Lines of the postprocessed file
			pathinfo -- Path information
			line -- Import line
		"""
		line	= line.replace('.', os.sep)
		line	= f'{line.strip()}.rebeca'
		return PreprocessorBase.process_import(self, result, pathinfo, line)

if __name__ == "__main__":
	test = PreProcessor()

