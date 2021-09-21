# Instance of Graph, Vertex, Edge
# Methods: add_node, add_edge, get_nodes, get_neighbors, size

from typing_extensions import ParamSpecKwargs


class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        '''
        add node
        Arguments: value
        Returns: The added node
        Add a node to the graph
        '''
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v


    def add_edge(self, start_vertex, end_vertex, weight=0):
        '''
        add edge
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        '''
        if start_vertex not in self._adjacency_list:
            raise KeyError('Starting Vertex not in Graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_nodes(self):
        '''
        get nodes
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        '''

    def get_neighbors(self):
        '''
        get neighbors
        Arguments: node
        Returns a collection of edges connected to the given node
            Include the weight of the connection in the returned collection
        '''

    def size(self):
        '''
        size
        Arguments: none
        Returns the total number of nodes in the graph
        '''

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex= vertex
        self.weight = weight