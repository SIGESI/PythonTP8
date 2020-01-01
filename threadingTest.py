import threading
import time

exitFlag = 0

class mThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__()
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("start thread:"+self.name)
        print_time(self.name,self.counter,5)
        print("quit thread"+self.name)


def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter-=1

thread1=