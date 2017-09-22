'''
Created on Sep 21, 2017

@author: andy
'''
import os

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if (os.path.isdir(sChildPath)):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
            

def printAn():
    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    print A0
    
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i:i*i for i in A1}
    A6 = [[i,i*i] for i in A1]

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print i*i
    print(l) 


if __name__ == '__main__':
    #print_directory_contents("c:")
    #printAn()
    f(2)
    f(3,[3,2,1])
    f(3)