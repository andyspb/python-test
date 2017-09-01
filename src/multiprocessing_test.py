'''
Created on Aug 28, 2017

@author: andy
'''

import threading


class SummingThread(threading.Thread):
    def __init__(self, low, high):
        super(SummingThread, self).__init__()
        self.low = low
        self.high = high
        self.total = 0
        
    def run(self):
        for i in range(self.low,self.high):
            self.total+=i

def test():
    print "test >>>"
    thread1 = SummingThread(0,500000)
    thread2 = SummingThread(500000,1000000)
    thread1.start() # This actually causes the thread to run
    thread2.start()
    thread1.join()  # This waits until the thread has completed
    thread2.join()  
    # At this point, both threads have completed
    print "thread1.total:", thread1.total
    print "thread2.total:", thread2.total
    result = thread1.total + thread2.total
    print "result:", result
    

if __name__ == '__main__':
    print "Multiprocessing test >>>"
    test()
    print "<<<"
