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

def main():
    matshow(a)
    show()

def shape_array():
    x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78]])
    print(np.shape(x))

if __name__ == '__main__':
    #main()
    shape_array()
