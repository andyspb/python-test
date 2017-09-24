'''
Created on May 3, 2017

@author: andy
'''

from plotly.zeppelin import iplot
from plotly.graph_objs import Scatter, Figure, Layout
import logging
 
def main():
    logging.info("From plotly test main() >>")
    num = 10
    xs = range(1,num)
    ys = map( lambda x : x*2 + 1, xs )
    iplot([{"x":xs, "y":ys}])
    
 

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()