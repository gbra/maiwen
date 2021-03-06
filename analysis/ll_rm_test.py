import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *

class ll_rm_test(Analysis): # define an analysis  

   def __init__(self):
	print  colored(' ' * self._indentation+"<b> Setting of the analysis : "+self.__class__.__name__, self._color)
	print colored(' ' * self._indentation+"**Running file: "+__file__, self._color)
	print  colored(' ' * self._indentation+"<e> Setting of the analysis : "+self.__class__.__name__, self._color)

   def analysis(self, model):
	print  colored(' ' * self._indentation+"<b> Analysis execution : "+self.__class__.__name__, self._color)

	#input data structures (model access)
	tasks_list=model.get("LIST_OF_TASKS")[0]
	
	#execute main test
	Sched=self.__ll_rm_test(tasks_list)

	#output data structure (model update)
	tasks_meta=model.get("TASKS_META")
	setattr(tasks_meta, 'isSched (RMA)', Sched)
	model.update("TASKS_META", tasks_meta)
	model.display("TASKS_META")

	print  colored(' ' * self._indentation+"<e> Analysis execution : "+self.__class__.__name__, self._color)
	return Sched

   def __ll_rm_test(self, tasks_list):
	print  colored(' ' * self._indentation+"Execute LL test...", self._color)

	#analysis implementation
  	_utilization_factor=0.0     	
	for task in tasks_list: 	
		print task.name, task.period, task.worst_case_execution_time, task.worst_case_execution_time/task.period
		_utilization_factor=_utilization_factor+float(task.worst_case_execution_time)/float(task.period)
	_tasks_nbr=float(len(tasks_list))	
	_test_bound=_tasks_nbr*(2.0**(1.0/_tasks_nbr)-1.0)  
    	if _utilization_factor<=_test_bound:
 		print  colored(' ' * self._indentation+"LL-test is satisfied, U is "+ str(_utilization_factor) +" <= "+ str(_test_bound) +" -> the tasks set is schedulable!", self._color)
		_Sched=True		
	else:
		print  colored(' ' * self._indentation+"LL-test is not satisfied, U is "+ str(_utilization_factor) +" > "+ str(_test_bound) +" -> unable to conclude about the tasks set!", self._color)		
		_Sched=False

	return _Sched

