#!/usr/bin/python
# Filename: Graph.py
# Description: Implementation of the Graph class

from compiler.lang.program.RuntimeObject import RuntimeObject
import heapq, json

class Edge:
	def __init__(self, id:str, to, weight:float=1.0, value=None):
		self.id		= id
		self.to		= to
		self.weight	= weight
		self.value	= value
		return
	
class Vertex:
	def __init__(self, id:str, value=None):
		self.id		= id
		self.value	= value
		self.edges	= []
		return
	
	def at(self, to):
		for edge in self.edges:
			if edge.to == to:
				return edge
		return None
	
	def join(self, edge:Edge):
		self.edges.append(edge)
		return edge
	
	def is_joined(self, to):
		if isinstance(to, Vertex):
			for edge in self.edges:
				if edge.to == to:
					return True
				
		elif isinstance(to, str):
			for edge in self.edges:
				if edge.to.id == to:
					return True
		return False
	
	def __eq__(self, rhs):
		return self.id == rhs.id

	def __ne__(self, rhs):
		return self.id != rhs.id

class Graph(RuntimeObject):
	def __init__(self):
		RuntimeObject.__init__(self)
		self.vertices	= []
		return

	@staticmethod
	def vtble(self):
		return {
			'add': self.add,
			'remove': self.remove,
			'find': self.find,
			'join': self.join,
			'find_arc': self.find_arc,
			'is_joined': self.is_joined,
			'nvertices': self.nvertices,
			'nedges': self.nedges,
			'pathto': self.pathto,
			'tostring': self.tostring,
			'fromstring': self.fromstring
		}
	
	def invoke(self, ctxt, method:str, args):
		return RuntimeObject.dispatch(self, [Graph.vtble(self)], method, args)

	def add(self, id:str, value=None):
		vertex = Vertex(id, value)
		self.vertices.append(vertex)
		return vertex

	def remove(self, vertex):
		self.vertices.remove(vertex)
		return
	
	def find(self, id:str):
		for vertex in self.vertices:
			if vertex.id == id:
				return vertex
		return None
	
	def join(self, id:str, start:str, end:str, value=None, weight:float=1.0):
		start	= self.find(start)
		end		= self.find(end)

		if start is None:
			return None
		
		edge 	= start.at(end)
		if edge is not None:
			edge.value = value
			return None

		return start.edges.append( Edge(id, end, weight, value) )

	def find_arc(self, start:str, end:str):
		start = self.find(start)
		if start is None:
			return None
		
		# Look for the edge in start's edges
		for edge in start.edges:
			if edge.to.id == end:
				return edge
		return None
	
	def is_joined(self, start:str, end:str):
		return True if self.find_arc(start, end) is not None else False
	
	def nvertices(self):
		return len(self.vertices)
	
	def nedges(self):
		total = 0
		for vertex in self.vertices:
			total += len(vertex.edges)
		return total
	
	def pathto(self, start:str, end:str):
		if isinstance(start, str):
			start 	= self.find(start)

		if isinstance(end, str):
			end 	= self.find(end)

		path	= Graph.__dijkstra(self, start, end)
		if path is None:
			return ''
		
		return ', '.join(path)

	@staticmethod
	def __dijkstra(graph, start, dest):
		vertices = graph.vertices

		# initialize known distance on the frontier
		dist 		= {v: (float('infinity'),None) for v in vertices}
		dist[start]	= (0, None)

		# Track a priority queue to pick the shortest next step
		pq 			= [(0, start)]
		current 	= start

		while len(pq):
			currdist, current = heapq.heappop(pq)

			if currdist > dist[current][0]:
				continue
			
			for next in current.vertices: 
				g 	= currdist + next.weight

				# If we have a better estimate, update 
				# distance map and priority queue
				if g < dist[next][0]:
					dist[next] = (g, current)
					if next == dest:
						pq.clear()
						break

					heapq.heappush( pq, (g, next) )


		# Build the path in reverse order
		path 		= []
		current 	= dest

		while current != start:
			partdist, prev = dist[current]
			current = prev
			path.append(current.id)

		path.append(start)
		return path

	def tostring(self):
		result = {}
		for vertex in self.vertices:
			result[vertex.id] = {
				'value': vertex.value,
				'edges': [ {'id': edge.id, 'to': edge.to.id, 'weight': edge.weight, 'value': edge.value} for edge in vertex.edges ]
			}
		return json.dumps(result, indent=2)
	
	def fromstring(self, data:str):
		obj 		= json.loads(data)
		result 		= Graph()
		
		for vid, vdata in obj.items():
			result.add(vid, value=vdata['value'])
			for edata in vdata['edges']:
				result.join( 
					edata['id'], 
					vid, 
					edata['to'], 
					edata['value'], 
					edata['weight']
					)
				
		return result
	
if __name__ == "__main__":
	test = Graph()
	test.add("A", value="Vertex A")
	test.add("B", value="Vertex B")
	test.add("C", value="Vertex C")

	test.join("E1", "A", "B", "Edge from A to B")
	edge = test.find_arc("A", "B")
	print(edge.value)  # Output: Edge from A to B
	print(test.is_joined("A","B"))
	print(test.is_joined("A","C"))
	print(test.tostring())

