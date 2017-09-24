'''
Created on Aug 28, 2017

@author: andy
'''

import Queue
import threading
import urllib2

theurls = ["http://google.com", "http://yahoo.com"]

def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

def test():
    print "Test"
    q = Queue.Queue()
    for u in theurls:
        t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

    s = q.get()
    print s

if __name__ == '__main__':
    print "Threading test >>>"
    test()
    
    print "<<<"
