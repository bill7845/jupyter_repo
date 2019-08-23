"""
    threading.Timer
        - 일정 시간 경과 후에 쓰레드 실행
"""

import time
import threading

def thread_func():
    for i in range(5):
        print('Thread....')

if __name__ == '__main__':
    t = threading.Timer(5, thread_func) # 5초후에 쓰레드를 시작
    t.start()

    # 3초후에 취소하면 5초후에 시작하려는 쓰레드가 취소되어 아무것도 출력되지 않는다
    #time.sleep(3)
    #t.cancel()