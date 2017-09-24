'''
Created on Apr 27, 2017

@author: andy
'''
import pandas as pd

import itertools

def expand_grid(data_dict):
    rows = itertools.product(*data_dict.values())
    return pd.DataFrame.from_records(rows, columns=data_dict.keys())

def test_pandas():
    df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
    print (df)
    df.ix[df.AAA >= 5,'BBB'] = -1; 
    print (df)
    
    df.ix[df.AAA >= 5,['BBB','CCC']] = 555; 
    print (df)

def main():
    numbers = [8, 42, 38, 111, 2, 39, 1];
    print (numbers, "\n");


if __name__ == '__main__':
    main()
