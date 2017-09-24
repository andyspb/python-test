'''
Created on May 1, 2017

@author: andy
'''

import logging
from logging.config import dictConfig
from enum import Enum, unique

class Log(object):
    INFO = 0
    DEBUG = 1
    ERROR = 2
    CRITICAL = 3
        
    def __init__(self, name = "None"):
        '''
        Constructor
        '''
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name) -2s %(levelname) -2s %(message)s',
                            datefmt='%d,%b %Y %H:%M:%S')

    def log(self, level, param):
        if level == Log.INFO:
            self.info(param)
        if level == Log.DEBUG:
            self.debug(param)
        if level == Log.ERROR:
            self.error(param)
        if level == Log.CRITICAL:
            self.critical(param)
    
    def info(self,param):
        self.logger.info(param)

    def debug(self,param):
        self.logger.debug(param)

    def error(self,param):
        self.logger.error(param)

    def critical(self,param):
        self.logger.critical(param)
         
        
def test():
    log = Log("TEST")
    log.log(Log.INFO, "(Log.INFO), Test log")
    log.info("Test info log")
    log.debug("Test debug log")
    log.error("Test error log")
    log.critical("Test critical log")
        
if __name__ == '__main__':
    test()
    