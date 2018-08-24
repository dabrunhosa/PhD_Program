from Mashes.IMashReader import IMashReader

class Skeleton(IMashReader):

    def version(self): return "1.0"
    
    def read(self,file): 
        raise NotImplementedError
        
        
        
        
# -*- coding: utf-8 -*-

