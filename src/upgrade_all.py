'''
Created on Sep 3, 2017

@author: andy
'''
import pip
from subprocess import call as c

def main():
    for dist in pip.get_installed_distributions():
        c("pip install --upgrade " + dist.project_name, shell=True)
    
if __name__ == '__main__':
    main()