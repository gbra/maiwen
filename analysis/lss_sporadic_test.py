import os, sys
from math import *
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *

class lss_sporadic_test(Analysis): # define an analysis  

   def __init__(self):
	print  colored(' ' * self._indentation+"<b> Setting of the analysis : "+self.__class__.__name__, self._color)
	print colored(' ' * self._indentation+"**Running file: "+__file__, self._color)
	print  colored(' ' * self._indentation+"<e> Setting of the analysis : "+self.__class__.__name__, self._color)

   def analysis(self, model):
	print  colored(' ' * self._indentation+"<b> Analysis execution : "+self.__class__.__name__, self._color)

	#input data structures (model access)
	periodic_tasks=model.get("LIST_OF_PERIODIC_TASKS")[1]
	aperiodic_server=model.get("TASKS_SERVER")[1]
	
	#execute main test
	Sched=self.__lss_sporadic_test(periodic_tasks, aperiodic_server)

	#output data structure (model update)
	#tasks_meta=model.get("TASKS_META")
	#setattr(tasks_meta, 'isSched (RMA)', Sched)
	#model.update("TASKS_META", tasks_meta)
	#model.display("TASKS_META")

	print  colored(' ' * self._indentation+"<e> Analysis execution : "+self.__class__.__name__, self._color)

	return Sched

   def __lss_sporadic_test(self, periodic_tasks, aperiodic_server):
	print  colored(' ' * self._indentation+"Execute %s..." %self.__class__.__name__, self._color)
	
	#computes maximum utilization of periodic tasks
	_periodic_utilization=0.0 
    	
	for task in periodic_tasks: 
		_periodic_utilization=_periodic_utilization+task.worst_case_execution_time/task.period

	#computes maximum utilization of aperiodic server
	_aperiodic_utilization=aperiodic_server.capacity/aperiodic_server.period    	

	#computes theoretical test bound
	_test_bound=log(2.0/(_aperiodic_utilization+1.0)) 

	#computes test 
    	if _periodic_utilization<=_test_bound:
 		print  colored(' ' * self._indentation+"%s is satisfied, U is " %self.__class__.__name__+ str(_periodic_utilization) +" <= "+ str(_test_bound) +" -> the tasks set is schedulable!", self._color)
		_Sched=True		
	else:
		print  colored(' ' * self._indentation+"%s is not satisfied, U is " %self.__class__.__name__+ str(_periodic_utilization) +" > "+ str(_test_bound) +" -> unable to conclude about the tasks set!", self._color)		
		_Sched=False

	return _Sched	


