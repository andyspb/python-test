'''
Created on Apr 27, 2017

@author: andy
'''

from multiprocessing import Process
import time

def worker(n):
    time.sleep(n)
    print n

def main():
    numbers = [8, 42, 38, 111, 2, 39, 1];
    print numbers, "\n";
    for n in numbers:
        p = Process(target = worker, args = (n, ))
        p.start()

if __name__ == '__main__':
    main()
