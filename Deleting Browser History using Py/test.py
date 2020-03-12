import sqlite3
import re

conn = sqlite3.connect('C:/Users/Mehul Trivedi/AppData/Local/Google/Chrome/User Data/Default/History')
cur = conn.cursor()

id = 0
result = True
var=input("Enter Keyword: ")
t='%'+var+'%'
while result:
    result = False
    ids=[]
    for row in cur.execute("SELECT id,url FROM urls WHERE url Like ?",(t,)):
        print(row)
        id = row[0]
        ids.append((id,))
    cur.executemany("DELETE FROM urls WHERE id = ? ",ids)
    print('============================================================================Deleted QUERY================================================================================================================================')
    conn.commit()
conn.close()
