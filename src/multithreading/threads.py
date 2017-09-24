'''
Created on Jul 29, 2015

@author: andy
'''
import Queue
import threading
import urllib2

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())


if __name__ == '__main__':
    theurls = ["http://google.com", "http://yahoo.com", "http://yandex.ru"]
    q = Queue.Queue()
    for u in theurls:
        t = threading.Thread(target=get_url, args = (q,u))
        t.daemon = True
        t.start()
    s = q.get()
    print s