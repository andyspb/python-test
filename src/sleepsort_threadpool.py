'''
Created on May 1, 2017

@author: andy
'''
import logging
import time
from multiprocessing.dummy import Pool as ThreadPool

sorted_numbers = []

def sort(number):
    time.sleep(number)
    print number
    sorted_numbers.append(number)

def main():
    logging.info("Sleepsort with threadpool >>>>")
    numbers = [1,4,3,5,8,7,13,26,55,14,2,9,12]
    logging.info(numbers)
    num = len(numbers)
    pool = ThreadPool(num) 
    pool.map(sort, numbers)

    pool.close()
    pool.join()

    logging.info(sorted_numbers)
    logging.info("<<< Sleepsort with threadpool")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()