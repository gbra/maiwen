import os, inspect, sys
from utils.termcolor import colored

from meta_accessors import Accessors
from data.data_structures import *
from data.data_model import *

class CPAL_accessors(Accessors):	

    dependency_graph={}	

    def __init__(self, directory):
    	'''Test function'''
	print colored(' ' * self._indentation+"Running script: "+__file__, self._color)
	print colored( ' ' * self._indentation+"Setting module: "+self.__class__.__name__, self._color)

    	#load rt-format file
	if len(os.listdir(directory))>0:
		i=0
		display=''
		model_list=[]
	    	for element in os.listdir(directory):
		    if not os.path.isdir(element) and  element.endswith('.rt-format'):
#			self.load_model.append(directory+'/'+element)
		    	# open rt-format file
			i+=1
			model_list.append(element)
			display+='('+str(i)+') '+element+' ' 
	else:
		print ' ' * self._indentation+ 'Loading CPAL (rt-format) file... No file model to load... Exit' 

	choice = raw_input(' ' * self._indentation+'Available instances are: '+display+'\r\n'+' ' * self._indentation+'Please choose a CPAL model instance (number)\n>');
	model=model_list[int(choice)-1]

	self.cpal_file = open(directory+'/'+model, "r")
	print ' ' * self._indentation+ 'Loading CPAL (rt-format) file... Successful'

    def ListOfTasks(self):
	print colored( ' ' * self._indentation+ "CPAL model access, getting: '"+inspect.stack()[0][3]+"' ", self._color)

#	cpal_file = open("rosace.rt-format", "r")

	#init list of tasks
	_list_of_tasks=[]
	_tasks_set=[]
	_task_name=_period=_best_case_execution_time=_worst_case_execution_time=_deadline=_offset=_priority=_respTime=_blockingTime=None
	
	# retrieve tasks and their properties from rt-format file
	for line in iter(self.cpal_file):
		if line.find("Task")!=-1:
			_task_name=self.__get_property_value_from_string(line, "name")		    				
			_worst_case_execution_time=int(self.__get_property_value_from_string(line, "wcet"))
			_period=int(self.__get_property_value_from_string(line, "period"))
			_offset=int(self.__get_property_value_from_string(line, "offset"))
			_deadline=int(self.__get_property_value_from_string(line, "deadline"))
			_tasks_set.append(Task(_task_name,_period,_best_case_execution_time,_worst_case_execution_time,_deadline,_offset,_priority,_respTime,_blockingTime))

	_list_of_tasks.append(_tasks_set)

	# close file
#	cpal_file.close()

	return _list_of_tasks

    def __get_property_value_from_string(self, str, prop_name):
	value=""
#	print "line: ", str
	index=str.find(prop_name)+len(prop_name+"=")
#	print "value found at index: ", index
	for i in range(index, len(str)):
		if (str[i] == ',') or (str[i] == '}'):
			break
		else:	
			value+=str[i]
#	print prop_name,"=",value
	return value

    def ListOfProcessors(self):
	print colored( ' ' * self._indentation+ "CPAL model access, getting: '"+inspect.stack()[0][3]+"' ", self._color)

    def TasksDependencies(self):
	print colored( ' ' * self._indentation+ "CPAL model access, getting: '"+inspect.stack()[0][3]+"' ", self._color)

	return self.dependency_graph

    def TasksServer(self):
	print colored( ' ' * self._indentation+ "CPAL model access: getting '"+inspect.stack()[0][3]+"' ", self._color)

