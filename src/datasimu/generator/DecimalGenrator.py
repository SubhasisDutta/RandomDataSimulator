'''
Created on Sep 6, 2015

@author: Subhasis
'''
import random
from datasimu.generator.FloatGenrator import FloatGenrator

class DecimalGenrator(object):
    '''
    classdocs
    '''


    def __init__(self, dataConf):
        '''
        Constructor
        '''
        self.dataConf=dataConf
    
    def getRandom(self):
        return round(FloatGenrator(self.dataConf).getRandom(),2)