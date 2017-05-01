'''
Created on May 1, 2017

@author: andy
'''
import logging
from multiprocessing.dummy import Pool as ThreadPool

def list_append(count, id, out_list):
    for i in range(count):
        rand = random.random()
        logging.info(rand)
        out_list.append(rand)

def main():
    logging.info("sleepsort with threadpool")
    numbers = [1,4,3,5,8,7,13,26,55,14,2,9,12]
    logging.info(numbers)
    num = len(numbers)
    pool = ThreadPool(num) 
    results = pool.map(list_append, my_array)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()