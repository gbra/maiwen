import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *
		
class classic_rm_MAST(Analysis):

   def __init__(self):
	print  colored(' ' * self._indentation+"--> Setting of the analysis : MAST-RMA", self._color)

   def analysis(self, model):
	""" 
	This function outsources the 'classic_rm' analysis to the MAST tool

	Arguments:
	model (DataModel): the data model 
	"""

	print  colored(' ' * self._indentation+"--> Analysis execution : RMA with MAST tool", self._color)
	
	# generate the MAST model from the data model
	self.generate_mast_input(model)
	
	# run the mast analysis with that generated model
	os.system("mast_analysis classic_rm mast-model.txt")

   def generate_mast_input(self, model):
	""" 
	This function generates a MAST model with Ocarina

	Arguments:
	model (DataModel): the data model 
	"""

	print  colored(' ' * self._indentation+"    **Executing OCARINA...", self._color)
  
	root_system=model.accessors.getAADLRoot()
	repository=model.accessors.load_model

	# build the Ocarina command to generate a MAST model from AADL
	cmd="ocarina -aadlv2 -g mast -r"
	path=os.getcwd()+"/"
	aadl_file=""
	for f in repository:
		aadl_file+=path+f+" "
	
	os.system(cmd+" "+root_system+" " +aadl_file)
