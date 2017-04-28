'''
Created on Apr 28, 2017

@author: andy
'''
import string
from random import *

def main() :
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 16)))
    print password
    

if __name__ == '__main__':
    main()