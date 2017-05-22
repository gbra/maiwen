import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *
from lib_context.lib_context import *

class srl_pcp_context(Analysis): # define an analysis  

   def __init__(self):
	print  colored(' ' * self._indentation+"<b> Setting of the analysis : "+self.__class__.__name__, self._color)
	print colored(' ' * self._indentation+"**Running file: "+__file__, self._color)
	print  colored(' ' * self._indentation+"<e> Setting of the analysis : "+self.__class__.__name__, self._color)

   def analysis(self, model):
	print  colored(' ' * self._indentation+"<b> Analysis execution : "+self.__class__.__name__, self._color)

	#input data structures (model access)
	tasks_list=model.get("LIST_OF_TASKS")[0]
	processors_list=model.get("LIST_OF_PROCESSORS")
	dependency_graph=model.get("TASKS_DEPENDENCIES")

	print  colored(' ' * self._indentation+"Check preconditions for SRL-PCP-test...", self._color)

	try:
		#check analysis preconditions
		assert (mono_processor(processors_list)),"multiprocessors architecture"
		assert (periodic_tasks(tasks_list)),"tasks are not periodic"
		assert (no_offsets(tasks_list)),"tasks have offsets"
		assert (implicit_deadlines(tasks_list)),"tasks have explicit deadlines"
		assert (fixed_computation_times(tasks_list)),"tasks have not fixed computation times"
		assert (not(independent_tasks(dependency_graph))),"tasks are independent"

		res=True
		print  colored(' ' * self._indentation+"OK", self._color)

	except AssertionError as e:
	    	print  ' ' * self._indentation,'precondition failed ', e.args
		res=False

	print  colored(' ' * self._indentation+"<e> Analysis execution : "+self.__class__.__name__, self._color)
	return res


