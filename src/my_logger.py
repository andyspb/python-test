'''
Created on May 1, 2017

@author: andy
'''

import logging
from logging.config import dictConfig


class Logger(object):
    '''
    classdocs
    '''
    def __init__(self, name = "None"):
        '''
        Constructor
        '''
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name) -4s %(levelname) -4s %(message)s',
                            datefmt='%d,%b %Y %H:%M:%S')
        
    def log(self,param):
        self.logger.info(param)