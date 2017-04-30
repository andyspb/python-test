'''
Created on Apr 30, 2017

@author: andy
'''

import logging
import threading
import time

def list_append(n, sorted_numbers):
    time.sleep(n)
    #print n
    sorted_numbers.append(n)


def main():
    logging.basicConfig(level=logging.INFO)
    numbers = [1,4,3,5,8,7,13,26,55,14,2,9,12]
    threads = len(numbers)
    
    for i in range (0, threads):
        out_list = list()
        thread = threading.Thread(target=list_append(size, i, out_list))
        jobs.append(thread)
    
    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

   
if __name__ == '__main__':
    main()