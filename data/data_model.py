import os, inspect, sys

from data_structures import *

class DataModel:

    data_model={}
    _indentation=0

    def __init__(self, accessors):
	print ' ' * self._indentation+"Running script: "+__file__
	print  ' ' * self._indentation+"Setting module: "+self.__class__.__name__+" with "+accessors.__class__.__name__

	#initialization with a design model
    	self.accessors=accessors

    def get(self, Id):
	print ' ' * self._indentation, "<b> DATA model ACCES"

	print ' ' * self._indentation, "Requires %s..." %Id
	#search for the data structure in data collection
	if Id in self.data_model:
		print ' ' * self._indentation, "%s found in data model..." %Id
		_data_struct=self.data_model.get(Id)

	#if not present, access to the design model
	else: 
		print ' ' * self._indentation, "%s not found in data model, call accessors..." %Id
		if (Id=="LIST_OF_TASKS") :
			_data_struct=self.accessors.ListOfTasks()
		elif (Id=="LIST_OF_PERIODIC_TASKS") :
			_data_struct=self.__ListOfPeriodicTasks()
		elif (Id=="LIST_OF_APERIODIC_TASKS") :
			_data_struct=self.__ListOfAperiodicTasks()
		elif (Id=="LIST_OF_PROCESSORS") :
			_data_struct=self.accessors.ListOfProcessors()
		elif (Id=="TASKS_DEPENDENCIES") :
			_data_struct=self.accessors.TasksDependencies()
		elif (Id=="TASKS_SERVER") :
			_data_struct=self.__TasksServer() 
		elif (Id=="TASKS_META") :
			_data_struct=Tasks_Meta()
		#update data model
		self.data_model[Id]=_data_struct

	#return data structure
	print ' ' * self._indentation, "<e> DATA model ACCESS"
	return _data_struct
	
    def update(self, Id, data_struct):
	print ' ' * self._indentation, "<b> DATA model UPDATE"
	print ' ' * self._indentation, "**update : added structure "+ Id

	self.data_model[Id].data=data_struct
	print ' ' * self._indentation, "<e> DATA model UPDATE"

#    def display(self):
#	print ' ' * self._indentation, "<b> DATA model display"

#	for e in self.data_model:
#		e.display()
#	print ' ' * self._indentation, "<e> DATA model display"

    def display(self, Id):
	print ' ' * self._indentation, "<b> DATA model display"
	print ' ' * self._indentation, "Displaying ", Id, "..."

	if hasattr(self.data_model[Id], '__iter__'):
		print ' ' * self._indentation, self.data_model[Id]
#		for e in self.data_model[Id]:
#			print ' ' * self._indentation, e.__str__
	else: 
		self.data_model[Id].display()

	print ' ' * self._indentation, "<e> DATA model display"

########################################	
#####			   	########
#####   high-level accessors 	########
#####				########
########################################

    def __TasksServer(self):
	print ' ' * self._indentation+ "--> high level accessor: getting '"+inspect.stack()[0][3]+"' "
	aperiodic_tasks=self.get("LIST_OF_APERIODIC_TASKS")
	periodic_tasks=self.get("LIST_OF_PERIODIC_TASKS")
	tasks_servers=[]
	
	for task_set in aperiodic_tasks:
		name=" server for (first aperiodic task) "+task_set[0].name
		capacity=0.0

		error=False

		for task in task_set:
			if task.worst_case_execution_time==None:
				print ' ' * self._indentation+"warning: unconsistant task set, execution time is missing for ", task.name
				error=True
				break
			else:
				capacity+=task.worst_case_execution_time

		if error==False:
			for task_set in periodic_tasks:
				period=[]
				for task in task_set:
					if task.period==None:
						print ' ' * self._indentation+"warning: unconsistant task set, period is missing for ", task.name
						error=True
						break
					else:
						period.append(task.period)
 
		if error==False:
			tasks_servers.append(Tasks_Server(name, min(period), capacity, "sporadic"))

		else:
			tasks_servers.append(Tasks_Server(name, None, None, None))			
	
#	for s in tasks_servers:
#		print "--------\nserver display\n-------- \nname:", s.name, "\nperiod: ", s.period, "\ncapacity: ", s.capacity,  "\nalgorithm: ", s.algorithm, "\n--------\n--------" 

	return tasks_servers	
	

    def __ListOfPeriodicTasks(self):
	print ' ' * self._indentation+ "--> high level accessor: getting '"+inspect.stack()[0][3]+"' "
	all_tasks=self.get("LIST_OF_TASKS")

	periodic_tasks=[]
	for t_set in all_tasks:
		print "******"
		task_set=[]
		for t in t_set:
			
			if t.period!=None: 
				print "period of %s is: " %t.name, t.period
				task_set.append(t)
		periodic_tasks.append(task_set)
	print "List of periodic tasks: ", periodic_tasks

	return periodic_tasks


    def __ListOfAperiodicTasks(self):
	print ' ' * self._indentation+ "--> high level accessor: getting '"+inspect.stack()[0][3]+"' "
	all_tasks=self.get("LIST_OF_TASKS")

	aperiodic_tasks=[]
	for t_set in all_tasks:
		print "*****"
		task_set=[]
		for t in t_set:
			if t.period==None: 
				print "period of %s is: " %t.name, t.period
				task_set.append(t)
		aperiodic_tasks.append(task_set)
	print "List of aperiodic tasks: ", aperiodic_tasks

	return aperiodic_tasks	 	 

