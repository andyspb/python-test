'''
Created on 10.03.2013

@author: andy
'''


def test():
    print reduce (lambda x, y: x + y, filter(lambda x: x % 2, map(lambda x: x * x, xrange (10 ** 6))))
    print sum(x * x for x in xrange(1, 10 ** 6, 2))
    print reduce(lambda x, y: x + y, filter(lambda x: x % 2, map(lambda x: x * x, xrange (10 ** 6)))) == sum(x * x for x in xrange(1, 10 ** 6, 2))

if __name__ == '__main__':
    test()
