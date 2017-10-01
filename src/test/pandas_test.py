#!/usr/bin/env python

##from (library) import (specific library function)
import sys  # only needed to determine Python version number

import matplotlib  # only needed to determine Matplotlib version number
from numpy import *
from pandas import DataFrame
import pylab

import matplotlib.pyplot as plt
import numpy_test as np
import pandas as pd


# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
x = np.arange(0, 5, 0.1)
y = np.sin(x)

# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

print df