#!/usr/bin/python
# Filename: PreProcessor.py
# Description: Implementation of the generic preprocessor class

import os

class PreProcessor:
	def __init__(self, includes=None):
		self.includes	= includes if includes is not None else []
		return

	def process(self, path):
		self.root		= os.path.dirname(path)	
		return self.__import_file(path)
	
	def __get_file(self, line):
		line    = line.strip()[6:]
		line	= line.replace('/', os.sep)
		return line.replace('\"', '').strip()

	def __resolve_abs_path(self, file:str):		
		# Check for absolute path
		if file.startswith(os.sep):
			if os.path.isfile(file) == False:
				raise FileNotFoundError(file)
			
			return file
		
		return None

	def __resolve_rel_path(self, parent:str, file:str):
		# Check if there are not relative path 
		if os.path.isfile(file):
			return file
		
		root	= os.path.dirname(parent)
		while file.startswith('..'):
			root	= os.path.pardir(root)

		file	= f'{root}{os.sep}{file}'
		if os.path.isfile(file) == False:
			return None

		return file
		
	def __resolve_file(self, parent:str, file:str):
		orig	= file
		file	= file.replace('/', os.sep)

		# If the import is an absolute path, then return it as is
		path 	= self.__resolve_abs_path(file)
		if path is not None:
			return path

		# Resolve relative path		
		path	= self.__resolve_rel_path(parent, file)
		if path is not None:
			return path
		
		# Search the include directories
		for root in self.includes:
			file	= f'{root}{os.sep}{file}'
			if os.path.isfile(file):
				return path

		raise FileNotFoundError(orig)
	
	def __import_file(self, path):
		result  = []
		
		with open(path) as file:
			lines   = [line.rstrip() for line in file]
			lineno  = 1

			for l in lines:
				# Handle all files that are not imports
				if l.startswith('import') == False:
					line	= self.process_line( (path,lineno), l)
					result.append( line )
					lineno  += 1
					continue

				self.process_import( result, (path,lineno), l )

				# Reset the line position to where we left off
				result.append(f'#line {lineno} {path}')

				lineno  += 1

		return result
		
	
	def process_line(self, pathinfo, line):
		return line

	def process_import(self, result, pathinfo, line):
		path 		= pathinfo[0]

		# Extract the file path and cannonicalize it
		import_file	= self.__get_file( line )
		import_path	= self.__resolve_file( path, import_file )

		# Set the line position to the start of the new file
		result.append(f'#line 0 {import_path}')

		# Append the imported file
		more    = self.__import_file( import_path )
		result.extend(more)

		return line

if __name__ == "__main__":
	test = PreProcessor()

