from abc import ABCMeta, abstractmethod

class IMashReader:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"
    
    @abstractmethod
    def read(self,file): raise NotImplementedError
