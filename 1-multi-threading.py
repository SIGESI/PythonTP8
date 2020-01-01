import threading
import time


def calcul_long(i):
    #time.sleep(1)
    n = 1E7
    while n>0:
        n -= 1
    print("calcul finish")
    print(threading.Thread.name)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=calcul_long,name="thread"+str(i),args=(i, )) #
        t.start()
        t.join()
        print(t.name)
        print(threading.current_thread())
        #print("thread "+str(i)+" start")
