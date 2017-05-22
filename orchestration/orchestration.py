from graph import *
from analysis import *

class Orchestration: 

    def __init__(self):
        """ initializes the analysis graph from contrats with SAT solvers """
	print "Calculate the analysis graph from contracts..."
#  	to implement contracts and SAT solvers with Python or mapping to Alloy

    def __init__(self, analysis_graph={}):
        """ alternative constructor: graph object is hardcoded """

	print "Calculate the analysis graph from contracts..."
	print "The analysis graph is hardcoded"

    	self.__graph = Graph(analysis_graph)
		
	print "The analyses to be used are:", self.__graph.__str__() 
#    	print "Check if graph is connected...", self.__graph.is_connected()
	

    def visit_graph(self, start, goal, data_model):

	visited=self.__graph.visit_bfs(start, goal, data_model)
	print "\nGraph execution [Node, Result]: ", visited

	success=False
	for v in visited:
		if goal in v[0]: 
			success=True

	return success

