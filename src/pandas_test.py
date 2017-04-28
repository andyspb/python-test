'''
Created on Apr 27, 2017

@author: andy
'''
##from (library) import (specific library function)
import pandas as pd
from pandas import DataFrame

import numpy as np
from numpy import *
# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import pylab


x = np.arange(0, 5, 0.1)
y = np.sin(x)

# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

print df