'''
Created on Apr 27, 2017

@author: andy
'''

from multiprocessing import Process
import time
import logging

sorted_numbers=[];

def worker(n):
    time.sleep(n)
    #print n
    sorted_numbers.append(n)

def main():
    logging.info("From main")
    numbers = [8, 42, 38, 111, 2, 39, 1];
    print numbers, "\n";
    for n in numbers:
        p = Process(target = worker, args = (n, ))
        p.start()
    print sorted_numbers, "\n";

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
