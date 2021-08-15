import re
import mysql.connector

email=input('email:')
valid=re.search(r'.*\@.[^\d]+\..+[^\d]',email)
while valid==None:
    print('it is wrong it should be like this:expression@string.string')
    email=input("try again:")
    valid=re.search(r'.*\@.[^\d]+\..+[^\d]',email)
email_password=input("password:")
db=mysql.connector.connect(
    user='root',password='your pass',host='127.0.0.1',database='your db'
)
cursor=db.cursor()

cursor.execute('INSERT INTO yourtable VALUES(\'%s\',\'%s\')'%(email,email_password))
db.commit()
print('done')