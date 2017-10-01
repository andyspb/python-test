#!/usr/bin/env python
'''
Created on Sep 3, 2017

@author: andy
'''


def fib(n):     # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


def fib2(n):    # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def main():
    print("fib(10):>>>>")
    n = 10
    print("fib2(", n, "): ", fib2(n))


if __name__ == '__main__':
    main()
