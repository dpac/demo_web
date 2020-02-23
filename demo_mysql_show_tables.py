import mysql.connector

mydb=mysql.connector.connect(
        host="webdemo.cbkr1mai5bui.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        passwd="cisco123",
       # database="mydatabase"
        database="web_demo"
        )
mycursor=mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
