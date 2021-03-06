from collections import Iterable

class Data_Struct:  

   _indentation=20

   def display(self):
	print ' ' * self._indentation, "Structure Type : " + self.__class__.__name__  
	for property, value in vars(self).iteritems():
    		print ' ' * self._indentation, property, ":", value

class Task(Data_Struct):  
   def __init__(self, name, period, best_case_execution_time, worst_case_execution_time, deadline, offset, priority, respTime, blockingTime):
	self.name=name
  	self.period=period
	self.best_case_execution_time=best_case_execution_time
	self.worst_case_execution_time=worst_case_execution_time
	self.deadline=deadline
	self.offset=offset
	self.priority=priority
   	self.respTime=respTime
	self.blockingTime=blockingTime

class Processor(Data_Struct):
  
   def __init__(self, name):
	self.name=name

   def display(self):
	print ' ' * self._indentation,  "Diplaying processor object - name : " + self.name   

class Schedulability: 
   _indentation=45 
   def __init__(self, schedulability, out_of_bound_tasks):
	self.schedulability=schedulability
	self.out_of_bound_tasks=out_of_bound_tasks

   def display(self):
	print ' ' * self._indentation, "Diplaying schedulability object - schedulability : " + self.schedulability + ", out of bound tasks : "+ str(self.out_of_bound_tasks).strip('')

class Tasks_Meta(Data_Struct):
   empty=None

class Tasks_Server(Data_Struct):
  
   def __init__(self, name, period, capacity, algorithm):
	self.name=name
	self.period=period
	self.capacity=capacity
	self.algorithm=algorithm


