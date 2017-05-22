import os, sys
import math
from utils.termcolor import colored

from meta_analysis import Analysis
from data.data_structures import *
		
class cheddar_simu(Analysis):

   def __init__(self):
	print  colored(' ' * self._indentation+"--> Setting of the analysis : Cheddar-Simu", self._color)

   def analysis(self, load_model):
	print  colored(' ' * self._indentation+"--> Analysis execution : Simulation with Cheddar tool", self._color)
	print  colored(' ' * self._indentation+"    **Executing OCARINA...", self._color)

