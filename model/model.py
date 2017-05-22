import os, inspect, sys
from utils.termcolor import colored

class Model:

    # for display
    _indentation=0
    _color='blue'


    directory=""
    model_type=""

    def __init__(self):
	print ' ' * self._indentation+ "Running script: "+__file__
	print  ' ' * self._indentation+ "Setting module: "+self.__class__.__name__
	#choose input model
	if len(os.listdir("model"))>0:
		i=0
		display=''
		model_list=[]
		for m in os.listdir("model"):
			if os.path.isdir('model/'+m):
				i+=1
				model_list.append(m)
				display+='('+str(i)+') '+m+' ' 
	else:
		print ' ' * self._indentation+'Error: No model is available for analysis... exit'
		sys.exit()

	choice = raw_input(' ' * self._indentation+'Available models are: '+display+'\r\n'+' ' * self._indentation+'Please choose a model (number)\n> ');
	self.directory='model/'+model_list[int(choice)-1]
	print colored( ' ' * self._indentation+ "Model directory is: "+ self.directory, self._color)

	# look for model type  	 
 	if self.directory.find('aadl') != -1:
		self.model_type="aadl"
		print ' ' * self._indentation+'Model type is: '+ self.model_type
 	elif self.directory.find('cpal') != -1:
 		self.model_type="cpal"
		print ' ' * self._indentation+'Model type is: '+ self.model_type
	else:
		print ' ' * self._indentation+'Error: unknown model type... exit'
		sys.exit()
		
