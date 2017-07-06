'''
Created on Jul 5, 2017

@author: andy

'''

from time import sleep

def print_decorator(function):
    def wrapper(*args, **kwargs):
        print "From print_decorator"
        return function(*args, **kwargs)
    return wrapper

def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        print "From wrapper(...)"
        sleep(2)
        return function(*args, **kwargs)
    return wrapper

@print_decorator
@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))