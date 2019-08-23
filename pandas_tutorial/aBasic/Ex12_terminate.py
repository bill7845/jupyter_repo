import os
import multiprocessing
import time

def func(tname):
    print('프로세스 %s : ' % (os.getpid()), tname)

def loopy(name):
    func('반복구문 시작')
    start = 1
    stop = 1000
    for num in range(start, stop):
        print('\t Number %s of %s' % (num, stop))
        time.sleep(1)

if __name__ == '__main__':
    func('나는 메인')
    p = multiprocessing.Process(target=loopy, args=('나는 반복구문',))
    p.start()
    time.sleep(10)
    p.terminate()
    print('메인종료')

