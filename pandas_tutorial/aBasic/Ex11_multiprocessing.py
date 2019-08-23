'''
    기존의 파이썬은 여러 모듈에서 프로세스를 다루는 함수와 메소드를 따로 제공하여 중복성이 심했다고 한다.
    파이썬은 multiprocessing 모듈이 thread 모듈보다 나중에 설계되었다고 한다.

    파이썬은 병렬처리를 위해 쓰레드를 사용하지 않고 multiprocessing 모듈을 사용한다.
    multiprocessing 모듈은 스레딩 모듈과 유사한 API를 사용한다.
    또한 스레드 대신 하위 프로세스를 사용하여 전역 인터프리터 잠금을 효과적으로 처리한다.
    유닉스 계열과 윈도우 모두 실행된다.
'''

import os
import multiprocessing

def func(tname):
    print('프로세스 %s : ' % (os.getpid()), tname)

if __name__ == '__main__':
    func('나는 메인')
    for n in range(4):
        p = multiprocessing.Process(target=func, args=('나는 별도의 프로세스',))
        p.start()
        # p.join() # 추후에 확인
    print('메인종료')

