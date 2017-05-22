from abc import ABCMeta, abstractmethod

class Analysis:        # defines abstract analysis
    __metaclass__ = ABCMeta
    _indentation=0
    _color='red'

    @abstractmethod
    def __init__(self):
	print colored('*' * self._indentation+"Running script: "+__file__, _color, attrs=['reverse', 'blink'])

    @abstractmethod
    def analysis(self):
      print  ' ' * self._indentation,"Analysis is not currently implemented"

