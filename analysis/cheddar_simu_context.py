import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *
from lib_context.lib_context import *

class cheddar_simu_context(Analysis): # define an analysis  

   def __init__(self):
	print  colored(' ' * self._indentation+"<b> Setting of the analysis : "+self.__class__.__name__, self._color)
	print colored(' ' * self._indentation+"**Running file: "+__file__, self._color)
	print  colored(' ' * self._indentation+"<e> Setting of the analysis : "+self.__class__.__name__, self._color)

   def analysis(self, model):
	print  colored(' ' * self._indentation+"<b> Analysis execution : "+self.__class__.__name__, self._color)

	#input data structures (model access)
	processors_list=model.get("LIST_OF_PROCESSORS")

	print  colored(' ' * self._indentation+"Check preconditions for Cheddar-Simu...", self._color)

	try:
		#check analysis preconditions
		assert (mono_processor(processors_list)),"multiprocessors architecture"

		res=True
		print  colored(' ' * self._indentation+"OK", self._color)

	except AssertionError as e:
	    	print  ' ' * self._indentation,'precondition failed ', e.args
		res=False

	print  colored(' ' * self._indentation+"<e> Analysis execution : "+self.__class__.__name__, self._color)
	return res


