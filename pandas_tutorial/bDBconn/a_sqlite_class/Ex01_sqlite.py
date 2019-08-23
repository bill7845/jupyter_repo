import sqlite3

"""
    [ 실행한 후에 SQLite Expert Person 에서 확인 ] 
    
    - 메뉴 > File > Open  Database 에서  db폴더 안에 testDB.db 연결
    - 탭팬들 확인 (Database / Data / DDL / Design / SQL )
    - SQL탭에서 select 문장 확인
    
    
    [ 절차 ]
        1. 데이타베이스 Connection 생성
        2. 커서 생성 ( 커서 : sql 명령어를 실행시켜 주는 객체 )
        3. sql 문장 만들기
        4. sql 문장 실행
        5. 커밋 ( 트랜젝션의 내용을 DB에 반영함 )
        6. Connection 닫기
    
"""

def viewTable(db, table):
    pass


def saveTest(db):
    pass

def saveTable(db, data):
    pass

def createTable(db):
    pass


if __name__ == '__main__':
    pass


    # (1) DB에 테이블 생성
    # createTable('../db/testDB.db')

    # (2) DB에 테이블 입력
    # saveTest('../db/testDB.db');  # 데이타 입력 확인만

    # (3) DB에 저장되어 있는 테이블값 출력
    # viewTable('../db/testDB.db', 'person')

