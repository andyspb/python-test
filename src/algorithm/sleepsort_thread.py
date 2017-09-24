'''
Created on Apr 30, 2017

@author: andy
'''

import logging
import threading
import time


def list_append(n, sorted_numbers):
    print (n)
    time.sleep(n)
    sorted_numbers.append(n)
    print (sorted_numbers)


def main():
    logging.basicConfig(level=logging.INFO)
    numbers = [1,4,3,5,8,7,13,26,55,14,2,9,12]
    logging.info(numbers)
    threads = len(numbers)
    jobs = []
    out_list = []
    for i in range (0, threads):
        t = threading.Thread(target=list_append(numbers[i], out_list))
        t.daemon = True
        jobs.append(t)
        t.start()
    
    # Start the threads (i.e. calculate the random number lists)
#     logging.info("Start jobs")
#     for j in jobs:
#         j.start()

#     Ensure all of the threads have finished
    for j in jobs:
        j.join()

    logging.info(out_list)
   
if __name__ == '__main__':
    main()