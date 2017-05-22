def get_property_value_from_string(str, prop_name):
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

# open rt-format file
fo = open("rosace.rt-format", "r")

# retrieve tasks and their properties 
for line in iter(fo):
	if line.find("Task")!=-1:
		print get_property_value_from_string(line, "name")		    				
		print int(get_property_value_from_string(line, "period"))
		print int(get_property_value_from_string(line, "wcet"))
		print int(get_property_value_from_string(line, "offset"))
		print int(get_property_value_from_string(line, "deadline"))

# close file
fo.close()
