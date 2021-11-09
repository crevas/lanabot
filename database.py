import sqlite3

# DB 생성
con = sqlite3.connect("memory.db")
# 커서 획득
cur = con.cursor()
#예제 sql문
sql1="CREATE TABLE ark(Id text,name text);"
sql2="INSERT INTO ark Values('gain_time@naver.com','myblog4');"
sql3="INSERT INTO ark Values('gain_time@naver.com','myblog4');"
sql4="INSERT INTO ark Values('gain_time@naver.com','myblog4');"
sql5="INSERT INTO ark Values('123123@naver.com','myblog4');"
sql6="INSERT INTO ark Values('444241@naver.com','myblog4');"
#sql실행.
cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)
cur.execute(sql4)
cur.execute(sql5)
cur.execute(sql6)
#commit
con.commit()
#데이터 확인해보기.
cur.execute('SELECT * FROM ark')
for row in cur:
    print(row)
#db연결해제.
con.close()
