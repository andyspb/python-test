#!/usr/bin/env python

import logging

logger = logging.getLogger('python-test')


def foo(bar):
    return bar + 1


def main():
    logging.info("Decorator test")
    print(foo(2) == 3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
