#!/usr/bin/env python

import logging

from plotly.graph_objs import Scatter, Figure, Layout
from plotly.zeppelin import iplot


def main():
    logging.info("From plotly test main() >>")
    num = 10
    xs = range(1, num)
    ys = map(lambda x: x * 2 + 1, xs)
    iplot([{"x": xs, "y": ys}])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
