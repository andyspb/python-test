'''
Created on May 2, 2017

@author: andy
'''

import logging

def f(x):
    return x**2

def main():
    logging.info("From main() >>>")
    print f(8)
    g = lambda x: x**2
    print g(8)
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    print foo
    print filter(lambda x: x % 3 ==0, foo)
    print reduce(lambda x,y: x+y, foo)
    nums = range (2,50)
    print nums
    for i in range(2,8):
        nums = filter(lambda x: x == i or x % i, nums)
    print nums
    sentence = 'It is raining cats and dogs'
    print sentence
    words = sentence.split()
    print words
    lengts = map(lambda word: len(word), words)
    print lengts

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()