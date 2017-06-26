try:
    import ocarina, lmp
except ImportError as error:
    print 'Import error: ', error, ', you will not be able to load AADL models'
    pass  

import os, inspect, sys
from utils.utils import *
from utils.termcolor import colored

from meta_accessors import Accessors
from data.data_structures import *
from data.data_model import *

class AADL_accessors(Accessors):	

    # temporary: hardcoded dependency graph representing independent tasks (requires to implement additional accessors)
    dependency_graph={"T1": [],
		 "T2": [],
		 "T3": [],	
	}	
    
    load_model=[]	
    aadl_root=None

    def __init__(self, directory):
    	'''Test function'''
	print colored(' ' * self._indentation+"Running script: "+__file__, self._color)
	print colored( ' ' * self._indentation+"Setting module: "+self.__class__.__name__, self._color)
    		# print all registered backends
#	print colored( "    **Checking backends"
#   	for backends in Backends:
#       		 print colored((backends);

    	#load aadl files
	if len(os.listdir(directory))>0:
	    	for element in os.listdir(directory):
		    if not os.path.isdir(element) and  element.endswith('.aadl'):
			self.load_model.append(directory+'/'+element)
	   		err=ocarina.load(self.load_model[-1]);                   # load a file
	    		print ' ' * self._indentation+ 'Loading AADL file... ', err
	else:
		print ' ' * self._indentation+ 'Loading AADL file... No file model to load... Exit ', err
    	err=ocarina.analyze();                         # analyze models
    	print ' ' * self._indentation+ 'Check AADL files... ', err
	if err[0]==False:
		print ' ' * self._indentation+'Error when checking file... exit'
		sys.exit() 
    	print ' ' * self._indentation+ 'Instantiate model... '
    	err=ocarina.instantiate("");           # instantiate system
    	print ' ' * self._indentation, err
	while err[0]!=True:
		choice = raw_input(' ' * self._indentation+'Please select a root system among choices\n> ')
#		choice ='paparazzi.basic_archi'
#		choice='paparazzi_system::paparazzi.pnp_tasks_interruptions'
		self.aadl_root=choice
#		print "hardcoded choice: ", choice
		err=ocarina.instantiate(choice);           # instantiate system
    		print ' ' * self._indentation, err		
	

    def ListOfTasks(self):
	print colored( ' ' * self._indentation+ "AADL model access, getting: '"+inspect.stack()[0][3]+"' ", self._color)
	#local variables
	_list_of_tasks=[]

	#exploration of the AADL Instance Tree
#	aadlInstances=lmp.getInstances('thread')[0]

	processes=lmp.getInstances('process')[0]
	threads=[]
	for t in lmp.getInstances('thread')[0]:
		threads.append(int(t))
    	print ' ' * self._indentation+ "Retrieving 'process' instances... found instances \t", processes

	for process in processes:
		task_set=[]
		subcomponents=ocarina.AIN.Subcomponents(process)[0]
    		print ' ' * self._indentation+ "Retrieving subcomponents... found instances \t", subcomponents
		print ' ' * self._indentation+ "Retrieving 'thread' instances...", subcomponents
		for s in subcomponents:	
			#if subcomponent is 'thread'
			if int(ocarina.AIN.Corresponding_Instance(s)[0]) in threads:
				task_set.append(self.__formatTaskFromNodeId(str(ocarina.AIN.Corresponding_Instance(s)[0])))

		# temporary: customized data model for mars pathfinder case study (requires to implement additional accessors)
		if 'pathfinder' in task_set[0].name: 
			blocking_time=2.1
			task_set[0].blockingTime=0.0
			task_set[1].blockingTime=blocking_time
			task_set[2].blockingTime=blocking_time
			task_set[3].blockingTime=0.0
			task_set[4].blockingTime=0.0
			task_set[5].blockingTime=blocking_time
			task_set[6].blockingTime=0.0

		_list_of_tasks.append(task_set)

	print "List of tasks: ", _list_of_tasks

	return _list_of_tasks

    def __formatTaskFromNodeId(self,nodeId):
	
	#init variables
	_task_name=_period=_best_case_execution_time=_worst_case_execution_time=_deadline=_offset=_priority=_respTime=_blockingTime=None

	#properties to get in the aadl instance model
	properties=['period', 'priority', 'deadline', 'compute_execution_time', 'dispatch_offset']
	property_value=None

	#get the task name
	_task_name=lmp.getInstanceName(nodeId)[0]

	#get the task properties values
	for prop in properties :
		#if the property is accessible
		if ocarina.getPropertyValueByName(nodeId,prop)[0][1] !=  ' KO':
			property_value=ocarina.getPropertyValueByName(nodeId,prop)[0][1]	
#				print colored( ' ' * self._indentation+ prop+'='+property_value, self._color)
			#values processing and storage
			for case in switch(prop):
			    if case('period'):
				_period=getValueFromAADLTime(property_value, 'us')
				break
			    if case('deadline'):
				_deadline=getValueFromAADLTime(property_value, 'us')
				break
			    if case('compute_execution_time'):
				_best_case_execution_time=getValueFromAADLTime(getAADLTimeFromAADLTimeRange(property_value, 'lower'), 'us')
				_worst_case_execution_time=getValueFromAADLTime(getAADLTimeFromAADLTimeRange(property_value, 'upper'), 'us')
				break
			    if case('dispatch_offset'):
				_offset=getTimeFromAADLString(property_value, 'us')
				break
			    if case('priority'):
				_priority=property_value
				break
			    if case(): # default, could also just omit condition or 'if True'
				print colored( ' ' * self._indentation+ "error: switch case is not covered", self._color)
#			else: 
#				print colored(  ' ' * self._indentation+ prop+' not found in the model!', self._color)
	
	return Task(_task_name,_period,_best_case_execution_time,_worst_case_execution_time,_deadline,_offset,_priority,_respTime,_blockingTime)

    def ListOfProcessors(self):
	print colored( ' ' * self._indentation+ "AADL model access, getting: '"+inspect.stack()[0][3]+"' ", self._color)
	_p1=Processor("p1")
	_list_of_processors=[_p1]	
	return _list_of_processors

    def TasksDependencies(self):
	print colored( ' ' * self._indentation+ "AADL model access, getting: '"+inspect.stack()[0][3]+"' ", self._color)

	#exploration of the AADL Instance Tree
#	aadlInstances=lmp.getInstances('thread')[0]

	processes=lmp.getInstances('process')[0]

	for process in processes:
		print ' ' * self._indentation,'Visiting ',lmp.getInstanceName(process)[0]
		print ' ' * self._indentation+ "Connection for %s: \t" %lmp.getInstanceName(process)[0], ocarina.AIN.Connections(process)
		connections=ocarina.AIN.Connections(process)[0]		
		i=0
		for c in connections:
			print "connection is: ", c			
			print "name is ", lmp.getInstanceName(c)
			print "corresponding instance is ", ocarina.AIN.Corresponding_Instance(c)
#			print "source is ", ocarina.AIN.Sources(str(ocarina.AIN.Corresponding_Declaration(c)[0]))
			print "source is ", ocarina.AIN.Sources(c)
			print "destination is ", ocarina.AIN.Destination(c)
			dest=ocarina.AIN.Destination(c)
			print "destination name is ", lmp.getInstanceName(dest)
			i+=1
			print "%d: connection: %s" %(i, lmp.getInstanceName(c)), ocarina.AIN.Corresponding_Instance(str(c))
		subcomponents=ocarina.AIN.Subcomponents(process)[0]
   		print ' ' * self._indentation+ "Retrieving subcomponents... found instances \t", subcomponents
		for sub in subcomponents:
			connected_components=ocarina.AIN.Connections(str(ocarina.AIN.Corresponding_Instance(sub)[0]))[0];
			print lmp.getInstanceName(str(ocarina.AIN.Corresponding_Instance(sub)[0]))
			print ' ' * self._indentation+ "**connection for %s: \t" %lmp.getInstanceName(sub)[0], connected_components


	
	"""sys.exit(0)"""
	"""#exploration of the AADL Instance Tree
	aadl_processes=lmp.getInstances('process')[0]
	subcomponents=None
	connected_components=None

	for p in aadl_processes:
		print ' ' * self._indentation,'Visiting ',lmp.getInstanceName(p)[0]
		subcomponents=ocarina.AIN.Subcomponents(p)[0];
   		print ' ' * self._indentation+ "**retrieving subcomponents... found instances \t", subcomponents
		connected_components=ocarina.AIN.Connections(p)[0];
    		print ' ' * self._indentation+ "**retrieving connections... found instances \t", connected_components

	for c in connected_components:
		#retrieve connected instances
		print 'Instance: ', c, ' is ', lmp.getInstanceName(c)[0]
		print 'Instance: ', c, ' is ', ocarina.AIN.Corresponding_Instance('311')[0]
		print 'Instance: ', c, ' is ', lmp.getInstances(c)[0]"""

	"""_dependency_graph={"T1": ["T2", "T3"],
		 "T2": ["T1", "T3"],
		 "T3": ["T1", "T2"],	
	}"""

	return self.dependency_graph

    def TasksServer(self):
	print colored( ' ' * self._indentation+ "AADL model access, getting: '"+inspect.stack()[0][3]+"' ", self._color)

    def getAADLRoot(self):
	print ' ' * self._indentation, "Request root system-> ", lmp.getRoot()[0]  
#	return lmp.getRoot()[0]
	return "mars_pathfinder::sys_mars_pathfinder.impl"
