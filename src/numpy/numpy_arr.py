'''
Created on Sep 3, 2017

@author: andy
'''

import numpy as np

def test():
    a = np.array([1, 2, 3])
    print "type(a)", type(a)
    print a

    b = np.array([[1.5, 2, 3], [4, 5, 6]])
    print b
    
    a0 = np.zeros((3, 5))
    print a0
    
    a1 = np.ones((4, 4))
    print a1
    
    a2 = np.empty((3,3))
    print a2
    
    a3 = np.eye(5)
    print a3
    
    print(np.arange(0, 3000, 1))

if __name__ == '__main__':
    test()