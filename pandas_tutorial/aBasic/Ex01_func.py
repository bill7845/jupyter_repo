"""
[ 파이썬에서 쓰레드 생성 방법 ]
1- threading.Thread의 생성자에 호출할 객체를 target으로 지정 ( 주로 사용되는 듯 )
2- threading.Thread의 서브클래스를 만들고 run() 오버라이딩   ( 우리에게 익숙 )

[ 파이썬 쓰레드의 특성 ]
    1. 파이썬은 GIL(Global Interpreter Lock) 특성의 제약사항으로
        파이썬의 스레드는 병렬 실행 효과를 가지지 않는다.
    2. 쓰레드는 종료하는 terminate() 함수가 없단다.
        ( 쓰레드에서 없다는 것이지 다른 대체 방식은 존재한다.
          지속적으로 발전하고 변경되기에 추후 상황을 다시 확인해야 합니다 )

"""

'''   
    파이썬 쓰레드의 주요 메소드
        - start()
        - run()
        - join()
        - getName()
        - setName()
        - is_alive()
        - isDaemon()
'''

import threading

def func( tname ):
    for n in range(5):
        print('쓰레드 %s : %d 번째 %s' % ( threading.current_thread(), n, tname ))


if __name__ == '__main__':
    # 1. 일반메소드 호출하듯이
    func('나는 메인')
    print('------------------------------------')

    # 2. 쓰레드 호출하듯이
    p = threading.Thread(target=func, args=('만든쓰레드',))
    p.start()
    print('\n메인종료')

'''
[참고] 자바처럼 sleep()메소드는 쓰레드이 있는 것이 아니라 time 모듈에 있는 거 사용해야 하나
    import time
    time.sleep(2)  - 2초
'''