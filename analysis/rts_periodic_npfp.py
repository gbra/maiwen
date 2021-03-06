import os, sys
import math
import linecache
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *
		
class rts_periodic_npfp(Analysis):

   def __init__(self):
	print  colored(' ' * self._indentation+"--> Setting of the analysis : Cheddar-Simu", self._color)

   def analysis(self, model):
	print  colored(' ' * self._indentation+"--> Analysis execution : analysis with RTS tool"+self.__class__.__name__, self._color)

	#input data structures (model access)
#	tasks_list=model.get("LIST_OF_TASKS")[1]
	tasks_list=model.get("LIST_OF_TASKS")[0]	#for CPAL

	#generates tool input file
	task_names=self.generate_input(tasks_list)
	#execute main test
	#Sched=self.__ll_rm_test(tasks_list)

	missed_deadlines=self.read_output(task_names)

	if len(missed_deadlines)==0:
 		print  colored(' ' * self._indentation+self.__class__.__name__+" test is successful, all deadlines are met", self._color)		
	else:
 		print  colored(' ' * self._indentation+self.__class__.__name__+" test failed, missed deadlines: "+', '.join(missed_deadlines), self._color)

	#output data structure (model update)

	#return Sched

   def generate_input(self, tasks_list):
	f = open("output/"+self.__class__.__name__+".rts", "w")
	
	#format file for rts tool
	task_names=[]
	for t in tasks_list:
		task_names.append(t.name)
#		task_names.append(t.name.replace('paparazzi.pnp_tasks_interruptions_airborne_autopilot_n_s_c_proc_',''))

	f.write('\nlayer single {policy=npfp; tasks: '+','.join(task_names)+';}\n\n');

	for t in tasks_list:
#		f.write('task %s {type=simple; T=%s; C=%s; D=%s;}\n'%(t.name.replace('paparazzi.pnp_tasks_interruptions_airborne_autopilot_n_s_c_proc_',''), str(int(t.period)), str(int(t.worst_case_execution_time)), str(int(t.period))));
		#for CPAL analysis, units changed from ps to ns
		f.write('task %s {type=simple; T=%s; C=%s; D=%s;}\n'%(t.name, str(int(t.period)/1000), str(int(t.worst_case_execution_time)/1000), str(int(t.period)/1000)));
	f.close()

	return task_names

   def read_output(self, task_names):
	filename="output/"+self.__class__.__name__+".html"
	f = open(filename, "r")

	n=0
	deadline=respTime=laxity=None
	missed_deadlines=[]
	for line in f:
		n+=1	
		for name in task_names:
			if name in line:
#			    	print "found line ", line
				deadline=int(filter(str.isdigit, linecache.getline(filename, n+3)))
				respTime=int(filter(str.isdigit, linecache.getline(filename, n+4)))
				laxity=deadline-respTime
#			    	print ' ' * self._indentation+"laxity for %s: %i" %(name, laxity) 
				if laxity < 0:
					missed_deadlines.append("laxity (%s)="%name+str(laxity))
	return missed_deadlines
			     
