from abc import ABCMeta, abstractmethod

class Accessors:
    __metaclass__ = ABCMeta
    _indentation=0
    _color='blue'

#    @abstractmethod
#    def __init__(self):

    def ListOfTasks(self):
        raise NotImplementedError()

	

