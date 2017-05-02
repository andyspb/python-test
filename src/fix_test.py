'''
Created on May 2, 2017

@author: andy
'''

from  my_logger import Logger

logger = Logger("fix_test")

def main():
    logger.log("From main >>>")

if __name__ == '__main__':
    main()