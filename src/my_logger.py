'''
Created on May 1, 2017

@author: andy
'''

import logging


class MyClass(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        self.logger = logging.getLogger("MyLogger")
        self.logger.basicConfig(logging.INFO)
        
    def log(self, param):
        self.logger.info(param)