try:
    import ocarina
except ImportError as error:
    print 'Import error: ', error, ', you will not be able to load AADL models'
    pass  

import sys

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def getValueFromAADLTime(aadl_time,output_unit):
 
    input_value=output_value=None
    input_unit=None	
    aadl_time_units=['ps', 'ns', 'us', 'ms', 'sec']

    #get input value nd input unit from aadl string value
    for _i in range(0, len(aadl_time_units)):
	    if aadl_time_units[_i] in aadl_time: 
		input_unit=aadl_time_units[_i]
		input_value=float(aadl_time.replace(input_unit,'')) 
		break 
#    print "value [input unit]=", input_value, input_unit

    #convert input value to base unit (ps)
    for case in switch(input_unit):
	    if case('ps'): 
		input_value=input_value*pow(10,0)
		break
	    if case('ns'): 
		input_value=input_value*pow(10,3)
		break
	    if case('us'):
		input_value=input_value*pow(10,6)
		break
	    if case('ms'):
		input_value=input_value*pow(10,9)
		break
	    if case('sec'):
		input_value=input_value*pow(10,12)
		break
	    if case(): # default, could also just omit condition or 'if True'
		print "switch case is not covered"
#    print "value [base unit]=", input_value, " ps"

    #convert input value to target unit
    for case in switch(output_unit):
	    if case('ps'):
		output_value=input_value*pow(10,0)
	    if case('ns'):
		output_value=input_value*pow(10,-3)
	    if case('us'):
		output_value=input_value*pow(10,-6)
		break
	    if case('ms'):
		output_value=input_value*pow(10,-9)
		break
	    if case('sec'):
		output_value=input_value*pow(10,-12)
		break
	    if case(): # default, could also just omit condition or 'if True'
		print "switch case is not covered"
#    print "value [output unit]=", output_value, output_unit

    return output_value

def getAADLTimeFromAADLTimeRange(aadl_time_range, case):
    lower_value=upper_value=''
    for _i in range(0, len(aadl_time_range)):
	if aadl_time_range[_i] != '.':
    		lower_value+=aadl_time_range[_i]
	else : 		
		for _j in range(_i+3, len(aadl_time_range)):
			upper_value+=aadl_time_range[_j]
		break
    if case == 'lower':
	return lower_value
    elif case == 'upper':
	return upper_value
    else : return None
	



