#!/usr/bin/env python

import logging
import random
import threading


def list_append(count, id, out_list):
    for i in range(count):
        rand = random.random()
        logging.info(rand)
        out_list.append(rand)


def main():

    size = 10000000   # Number of random numbers to add
    threads = 2   # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=list_append(size, i, out_list))
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

    print("List processing complete.")
    print(out_list)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
