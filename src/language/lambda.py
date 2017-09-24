'''
Created on Apr 23, 2017

@author: andy
'''

def test(a):
    print (a)
    m = map( lambda x : x*2 + 1, a )
    print (list(m))    

def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)

def test2():
    (a, *rest, b) = range(5)
    print (a,rest,b)
    
def foo(a, b_c):
    #b,c = b_c
    print(b_c)

def tuple_test():
    a = tuple('Hello, world')
    print(a)
    a = ('s')
    print(a)
    a = tuple()
    print(a)

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    #test(a)
    #outer()
    #test2()
    #foo(1,(1,2,3))
    tuple_test()