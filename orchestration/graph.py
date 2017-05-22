class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def is_connected(self, 
                     vertices_encountered = None, 
                     start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict        
        vertices = list(gdict.keys()) # "list" necessary in Python 3 
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

    def find_path(self, start_vertex, end_vertex, path=[]):
        """ find a path from start_vertex to end_vertex 
            in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

    def visit_bfs(self, start, goal, data_model):
	""" visit graph according to bfs algorithm """
	print "Visiting the graph according to the bfs algorithm... "

#	visited, queue = {start :None}, [start]
	queue=[start]
	visited=[]
	i=0

	# compute queue
	while queue :
		i += 1
		print "\n** Iteration ", i

		# execute first node in queue
		root_node=queue.pop(0)

		if (isinstance(root_node, str)): root_name=root_node
		else: root_name=root_node.__class__.__name__

		print "Execute node %s..." %root_name
		result=self.__exec_node(root_node, data_model)
		visited.append([root_name, result])

		print 'Prepare graph...'
		# true or other results = normal mode
		if result!=False:
			# look for adjacent nodes
			for adjacent_node in self.__graph_dict[root_node] :

				# adjacent node found
				if (isinstance(adjacent_node, str)): adjacent_name=adjacent_node
				else: adjacent_name=adjacent_node.__class__.__name__
				print "Adjacent node found... ", adjacent_name

				# skip if adjacent node already in queue
				if adjacent_node in queue :
					print '%s already in execution queue, skip' %adjacent_node.__class__.__name__ 
					continue

				# add adjacent node in queue else
#				visited[adjacent_node]=root_node
				queue.append(adjacent_node)
				print "%s added in queue for execution" %adjacent_node.__class__.__name__
		# false result = pre analysis is not verified  		
		else:
			print "%s test is not verified" %root_name
			# delete adjacent nodes from queue
			for adjacent_node in self.__graph_dict[root_node] :
				if adjacent_node in queue:
					print "Update execution queue... adjacent node deleted from queue:", queue.remove(adjacent_node)

			# delete subsequent paths
			print 'Update graph... delete subsequent paths...'
			delete_paths=self.find_all_paths(root_node, goal)
			self.__delete_paths(delete_paths)

	print "End of graph: no more analysis to execute"
	return visited

    def __exec_node(self, node, data_model):
	result=None
	analysis_method = getattr(node, "analysis", None)
	if callable(analysis_method):
		result=node.analysis(data_model)
	else: 
		print node, ' is not an executable node'
	return result

    def __delete_paths(self, paths_list):
#        print "graph :", self.__graph_dict
#	print "paths deleted from graph: ", paths_list
	for path in paths_list:
        	for vertex in self.__graph_dict:
            		if vertex in path: 
				self.__graph_dict[vertex]=[]
#				print "deleted adjency list for:", vertex 
        print "Modified graph:", self.__graph_dict
        
    def __str__(self):
        res = ""
        for vertex in self.__graph_dict:
            res += vertex.__class__.__name__+", " 
#        res += "\nedges: "
#        for edge in self.__generate_edges():
#            res += str(edge) + " "
        return res

