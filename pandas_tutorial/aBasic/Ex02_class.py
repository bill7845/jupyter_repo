import threading

class MyThread(threading.Thread):  # threading.Thread 클래스 상속

    def __init__(self, tname):
        threading.Thread.__init__(self)  # 반드시 부모 함수 호출하여 (기본값 초기화해야 한다)
        self.tname = tname

    def run(self):  # 오버라이딩
        for i in range(50):
            print( self.tname + ":" + str(i))
            # print( self.tname, ' : ', str(i)) # 문자열 붙이는 방식과 다르군 ( 이거실행 range(5)만해도 됨 )

if __name__ == '__main__':
    t1 = MyThread('차틀만들기')
    t2 = MyThread('엔진부착')
    t1.start()
    t2.start()

    """
    # print('------------ main 함수 종료--------------')
    t1.join()
    t2.join()
    print('------------ main 함수 종료--------------')
    """

'''
[참고] 동기화를 하기 위해 threading.Event() 사용하면 된다지만 
'''