import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *

class srl_pcp_test_cor17(Analysis): # define an analysis  

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
	Sched=self.__srl_pcp_test_corollary17(tasks_list)

	#output data structure (model update)
	#tasks_meta=model.get("TASKS_META")
	#setattr(tasks_meta, 'isSched (RMA)', Sched)
	#model.update("TASKS_META", tasks_meta)
	#model.display("TASKS_META")

	print  colored(' ' * self._indentation+"<e> Analysis execution : "+self.__class__.__name__, self._color)

	return Sched


   def __srl_pcp_test_corollary17(self, tasks_list):
	print  colored(' ' * self._indentation+"Execute SRL-PCP-test (corollary17)...", self._color)
	
	#analysis implementation
	res=None
	ab=0

	#test completion
	for i in range(0, len(tasks_list)):
		task_i=tasks_list[i]
  		utilization_factor=(task_i.worst_case_execution_time+task_i.blockingTime)/task_i.period

		for k in range(0, i):
			task_k=tasks_list[k]
			utilization_factor+=task_k.worst_case_execution_time/task_k.period

		test_bound=float(i+1)*(2.0**(1.0/float(i+1))-1.0) 
	    	if utilization_factor<=test_bound:
	 		print  colored(' ' * self._indentation+"SRL-PCP-test is satisfied for task %s, U=%f <= %f -> the tasks set is schedulable!" %(task_i.name, utilization_factor, test_bound), self._color)
		else:
			print  colored(' ' * self._indentation+"SRL-PCP-test is not satisfied task %s, , U=%f > %f -> unable to conclude about the tasks set!" %(task_i.name, utilization_factor, test_bound), self._color)		
			ab+=1

	#when test is completed
	if ab==0:
		print ' ' * self._indentation, "SRL-PCP-test (corollary17) successful -> the system is schedulable!"
		res=True
	else: 
		print ' ' * self._indentation, "SRL-PCP-test (corollary17) failed %d times -> unable to conclude about the tasks set!" %ab
		res=False
	return res

