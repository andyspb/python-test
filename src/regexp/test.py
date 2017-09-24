'''
Created on Sep 23, 2017

@author: andy
'''
import re

def test():
    p = re.compile('ab*')
    m = p.findall('absolutely abab') 
    print (m)

if __name__ == '__main__':
    test()