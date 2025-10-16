#!/usr/bin/python
# Filename: Factory.py
# Description: Implementation of the Factory class

from compiler.lang.rebeca.Actor import Actor
from compiler.lang.objects.List import List
from compiler.lang.objects.Map import Map
from compiler.lang.objects.Stack import Stack
from compiler.lang.objects.Queue import Queue
from compiler.lang.objects.PriorityQueue import PriorityQueue
from compiler.lang.objects.Tree import Tree
from compiler.lang.objects.Port import Port

from abc import ABC, abstractmethod

class Factory:
	def __init__(self):
		return

	def create_actor(self, ctxt, rc, name:str, idents:list=None, params:list=None):
		return Actor(ctxt, rc, name, idents, params)
		
	def create_object(self, ctxt, type:str):			
		if type == 'map':
			return Map()
		elif type == 'list':
			return List()
		elif type == 'stack':
			return Stack()
		elif type == 'queue':
			return Queue()
		elif type == 'heap':
			return PriorityQueue()
		elif type == 'tree':
			return Tree()
		elif type == 'port':
			return Port()
		return None
	
if __name__ == "__main__":
	test = Factory()

