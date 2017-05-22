"""from os.path import dirname, basename, isfile
import glob
import importlib

#dynamically import all modules in directory
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f)]
for m in __all__: 
	importlib.import_module(m)"""

from model import *
