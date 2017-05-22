
def mono_processor(processors_list):
	if len(processors_list) != 1 : return False
	return True

def periodic_tasks(tasks_list):
    	for task in tasks_list:
		if type(task.period) != int and type(task.period) != float:
            		return False
  	return True 	

def no_offsets(tasks_list):
    	for task in tasks_list:
		if task.offset >= 0:
            		return False
		if task.offset >= 0.0:
            		return False
  	return True

def implicit_deadlines(tasks_list):
    	for task in tasks_list:
		if task.deadline != None and task.deadline != task.period:
            		return False
  	return True

def fixed_computation_times(tasks_list):
    	for task in tasks_list:
		if task.worst_case_execution_time != None and task.worst_case_execution_time > task.period:
            		return False
  	return True

def independent_tasks(dependency_graph):
	for task in dependency_graph:
		dependent_tasks=dependency_graph[task] 
		if len(dependent_tasks) > 0: 
			return False
	return True
