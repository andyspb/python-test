#!/usr/bin/env python

import logging
from multiprocessing.dummy import Pool as ThreadPool

import urllib2


def test(url):
    logging.info("From test >>>>")
    logging.info(url)
    urllib2.urlopen(url)
    logging.info("<<<<")


def main():
    logging.info("From main() >>>>")
    urls = [
        'http://www.python.org',
        'http://www.python.org/about/',
        'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
        'http://www.python.org/doc/',
        'http://www.python.org/download/',
        'http://www.python.org/getit/',
        'http://www.python.org/community/',
        'https://wiki.python.org/moin/',
    ]
    # Make the Pool of workers
    pool = ThreadPool(4)
    # Open the urls in their own threads
    # and return the results
    # close the pool and wait for the work to finish
    results = pool.map(test, urls)
    pool.close()
    pool.join()
    logging.info("<<<< main")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
