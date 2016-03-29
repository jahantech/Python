#!/usr/bin/python

import threading
import time

class NewThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadID = name
    def run(self):
        print "Starting New Thread: " + self.name        # Get lock to synchronize threads
        threadLock.acquire()
        Product_Number(self.name, self.counter)
        threadLock.release()

def Product_Number(threadName, delay):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []
counter = 10
# Create new threads
thread1 = myThread(1, "Processing Thread 1")
thread2 = myThread(2, "Processing Thread 2")

# Start threads
thread1.start()
thread2.start()

# Add threads to workgroup 
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"
