import sqlite3
import csv

def createDBtable(db):
    pass

def saveDBtable(db, data):
    pass

def viewDBdata(db, table):
    pass


if __name__ == '__main__':

    db_name = '../db/supplyDB.db'

    # (1) DB에 테이블 생성
    # createDBtable(db_name)

    # ------------------------------------------------------
    # (2) csv파일을 읽어서 DB에 테이블 입력
    # file_name='../files/supply.csv'
    # file = csv.reader(open(file_name,'r'), delimiter=',')


    # ------------------------------------------------------
    # (3) DB에 저장되어 있는 테이블값 출력
    # viewDBdata(db_name, 'supply') # 디비명, 테이블명
