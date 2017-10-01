#!/usr/bin/env python
'''
Created on Apr 27, 2017

@author: andy
'''

import logging
from multiprocessing import Process
import time


sorted_numbers = []


def worker(n):
    time.sleep(n)
    # print n
    sorted_numbers.append(n)


def main():
    logging.info("From main")
    numbers = [8, 42, 38, 111, 2, 39, 1]
    print(numbers)
    for n in numbers:
        p = Process(target=worker, args=(n, ))
        p.start()
    print(sorted_numbers)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
