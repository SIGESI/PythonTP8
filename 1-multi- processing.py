from multiprocessing import Process

def calcul_long():
    n = 1E7
    while n>0:
        n -= 1
    print("calcul finish")
    print(Process.name)

if __name__ == '__main__':
    for i in range(5):
        p = Process(target=calcul_long(), args=('bob',),name="process "+str(i))
        p.start()
        p.join()
        print(p.name)
        #print("thread "+str(i)+" start")
