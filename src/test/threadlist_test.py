#!/usr/bin/env python

from random import randint
import threading
from time import sleep


thread_list = []


def print_number(num):
    # sleeps a random 1 to 10 seconds
    r = randint(1, 10)
    sleep(r)
    print("Thread " + str(num) + " slept for " + str(r) + " seconds")


def test():
    print("Start.>>>")
    print("a"
          "b"
          "c")
    print("""
a
b
c
""")
    for i in range(1, 10):
        t = threading.Thread(target=print_number, args=(i,))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    print("Done.<<<")


if __name__ == '__main__':
    print("From threadlist_test")
    test()
