import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *

class srl_pcp_test_th16(Analysis): # define an analysis  

   def __init__(self):
	print  colored(' ' * self._indentation+"<b> Setting of the analysis : "+self.__class__.__name__, self._color)
	print colored(' ' * self._indentation+"**Running file: "+__file__, self._color)
	print  colored(' ' * self._indentation+"<e> Setting of the analysis : "+self.__class__.__name__, self._color)

   def analysis(self, model):
	print  colored(' ' * self._indentation+"<b> Analysis execution : "+self.__class__.__name__, self._color)

	#input data structures (model access)
	tasks_list=model.get("LIST_OF_TASKS")[0]
#	tasks_list=[Task("t1",100.0,40.0,40.0,None,None,None,None,20), Task("t2",150.0,40.0,40.0,None,None,None,None,30.0), Task("t3",350.0,100.0,100.0,None,None,None,None,0.0)]

	#execute main test
	Sched=self.__srl_pcp_test_theorem16(tasks_list)

	#output data structure (model update)
	#tasks_meta=model.get("TASKS_META")
	#setattr(tasks_meta, 'isSched (RMA)', Sched)
	#model.update("TASKS_META", tasks_meta)
	#model.display("TASKS_META")

	print  colored(' ' * self._indentation+"<e> Analysis execution : "+self.__class__.__name__, self._color)

	return Sched

   def __srl_pcp_test_theorem16(self, tasks_list):
	print  colored(' ' * self._indentation+"Execute SRL-PCP-test (theorem16)...", self._color)
	
	#analysis implementation
  	utilization_factor=0.0
	res=None
     	blockingTime_factor=[]
	test_bound=float(len(tasks_list))*(2.0**(1.0/float(len(tasks_list)))-1.0) 
	
	for task in tasks_list: 
		utilization_factor+=task.worst_case_execution_time/task.period
		blockingTime_factor.append(task.blockingTime/task.period)	
 
	print ' ' * self._indentation, "max blocking time factor=", max(blockingTime_factor)

    	if utilization_factor+max(blockingTime_factor)<=test_bound:
 		print  colored(' ' * self._indentation+"SRL-PCP-test is satisfied, U=%f <= %f -> the tasks set is schedulable!" %((utilization_factor+max(blockingTime_factor)), test_bound), self._color)
		res=True		
	else:
		print  colored(' ' * self._indentation+"SRL-PCP-test is not satisfied, , U=%f > %f -> unable to conclude about the tasks set!" %((utilization_factor+max(blockingTime_factor)), test_bound), self._color)		
		res=False
	return res

