import mysql.connector

mydb=mysql.connector.connect(
        host="webdemo.cbkr1mai5bui.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        passwd="cisco123"
)
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

