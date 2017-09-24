'''
Created on Sep 23, 2017

@author: andy
'''

def test():
    num = 20
    a = sum(range(num))
    print(a)
    
    b = (num*(num-1))>>1
    print (b)
    
    l = list(range(num))
    print (l)
    
    word = "hello"
    new_list = [x for x in word]
    print (new_list)
    
    new_list = [num for num in range(30) if num % 3 == 0]
    print (new_list)

if __name__ == '__main__':
    test()