'''
Created on Apr 27, 2017

@author: andy
'''

from numpy import *
a = arange(15).reshape(3, 5)
print "The matrix a is \n"+str(a)
print "a[1,2] = " +str(a[1,2])
print "the matrix dimension is " + str(a.shape)

from matplotlib.pyplot import *
from pylab import *
matshow(a)
show()