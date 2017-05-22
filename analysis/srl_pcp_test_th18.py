import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *

class srl_pcp_test_th18(Analysis): # define an analysis  

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
	Sched=self.__srl_pcp_test(tasks_list)

	#output data structure (model update)
	#tasks_meta=model.get("TASKS_META")
	#setattr(tasks_meta, 'isSched (RMA)', Sched)
	#model.update("TASKS_META", tasks_meta)
	#model.display("TASKS_META")

	print  colored(' ' * self._indentation+"<e> Analysis execution : "+self.__class__.__name__, self._color)

	return Sched

   def __srl_pcp_test(self, tasks_list):
	print  colored(' ' * self._indentation+"Execute SRL-PCP test (theorem18)...", self._color)
	
	err=0
	ab=0
	res=None

	#analysis implementation  	
	for i in range(0, len(tasks_list)):
		task_i=tasks_list[i]
#		print ' ' * self._indentation, "i: ", i, "(considered task is print %s)" %task_i.name 
		result_k=[]
		for k in range(0, i+1):
			result_j=0.0
			task_k=tasks_list[k]
#			print ' ' * self._indentation, "     -> k: ", k, "(considered task is print %s)" %task_k.name
			l=math.floor(task_i.period/task_k.period)
#			print ' ' * self._indentation, "     -> calculated l is: ", task_i.period, "/", task_k.period, "=", l 
			if l!=0.0:
				for j in range(0, i):
					task_j=tasks_list[j]
#					print ' ' * self._indentation, "          -> j: ", j, "(considered task is print %s)" %task_j.name
					u=task_j.worst_case_execution_time/task_j.period
					result0=u*(task_j.period/(l*task_k.period))
#					print ' ' * self._indentation, "          -> calculated result (0) is: ", result0
					result0bis=(math.ceil(l*task_k.period/task_j.period))
#					print ' ' * self._indentation, "          -> calculated result (0bis) is: ", result0bis
					result1=result0*result0bis
#					print ' ' * self._indentation, "          -> calculated result (1) is: ", result1
					result2=((task_i.worst_case_execution_time+task_i.blockingTime)/(l*task_k.period))
#					print ' ' * self._indentation, "          -> calculated result (2) is: ", result2 
					result_j+=result1+result2
#				print  ' ' * self._indentation, "          -> result=", result_j  
				result_k.append(result_j)
			else:
 				print "Error: Float division by zero... Skip operation"
				err+=1

#			print ' ' * self._indentation, "     -> min value in k is: ", min(result_k) 	
		
		if min(result_k)>1:
			print ' ' * self._indentation, "PCP-test not verified -> min value at iteration i=%d k=%d is %f > 1.0" % (i, k, min(result_k)) 
			ab+=1

	print ' ' * self._indentation, "Number of errors: %d - number of abortions %d" % (err, ab)

	if ab==0:
		print ' ' * self._indentation, "SRL-PCP test (theorem18) successful -> the system is schedulable!"
		res=True
	else: 
		print ' ' * self._indentation, "SRL-PCP test (theorem18) failed %d times -> unable to conclude about the tasks set!" %ab
		res=False
	return res

