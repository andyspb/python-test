'''
Created on May 2, 2017

@author: andy
'''

import logging

def main():
    logging.info("From main() >>>")
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()