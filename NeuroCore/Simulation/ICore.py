# -*- coding: utf-8 -*-
'''
Created on August 24, 2017

@author: dabrunhosa
'''

from abc import ABCMeta, abstractmethod

class ICore(object):
    
    ########################################
    ###       Private Variables          ###
    ######################################## 
    
    # Setting this class as an abstract class
    __metaclass__ = ABCMeta
    
    ########################################
    ###          Constructor             ###
    ######################################## 
    
    def __init__(self, global_conditions=None, name="core"):
        if global_conditions is None:
            global_conditions = list()
        self.__global_conditions = global_conditions
        self.__name = name
   
    ########################################
    ###       Class Functions            ###
    ######################################## 

    @classmethod
    def version(self): return "1.0"
    
    ########################################
    ###       Abstract Functions         ###
    ######################################## 
    
    @abstractmethod
    def solve(self):
        raise NotImplementedError
