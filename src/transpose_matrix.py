'''
Created on Apr 28, 2017

@author: andy
'''

import numpy as np

def main():
    m = [[1,2],[3,4],[5,6]]
    for row in m :
        print(row)
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print("\n")
    for row in rez:
        print(row)

def zip_test():
    matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
    for row in matrix:
        print(row)
    print("\n")
    t_matrix = zip(*matrix)
    for row in t_matrix:
        print row

def numpy_test():
    matrix=[[1,2,3],[4,5,6]]
    print(matrix)
    print("\n")
    print(np.transpose(matrix))

if __name__ == '__main__':
    #main
    #zip_test()
    numpy_test()