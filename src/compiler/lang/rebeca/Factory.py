#!/usr/bin/python
# Filename: Factory.py
# Description: Implementation of the Factory class

from compiler.lang.rebeca.Actor import Actor
from compiler.lang.objects.List import List
from compiler.lang.objects.Map import Map
from compiler.lang.objects.Stack import Stack
from compiler.lang.objects.Queue import Queue
from compiler.lang.objects.Graph import Graph
from compiler.lang.objects.PriorityQueue import PriorityQueue
from compiler.lang.objects.Tree import Tree
from compiler.lang.objects.Port import Port
from compiler.lang.objects.StateMachine import StateMachine

from abc import ABC, abstractmethod

class Factory:
	def __init__(self, interfaces:dict= None):
		self.set_config(interfaces)
		return

	def set_config(self, interfaces:dict):
		self.iport =	interfaces.get('port') if interfaces else None
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
		elif type == 'graph':
			return Graph()		
		elif type == 'port':
			return Port(self.iport)
		elif type == 'fsm':
			return StateMachine()
		return None
	
if __name__ == "__main__":
	test = Factory()

