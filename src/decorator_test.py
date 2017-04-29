'''
Created on Apr 29, 2017

@author: andy
'''

import logging

logger = logging.getLogger('python-test')

def main():
    logging.info("Decorator test")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()