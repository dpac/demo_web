import mysql.connector

mydb=mysql.connector.connect(
        host="webdemo.cbkr1mai5bui.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        passwd="cisco123",
        database="mydatabase"
        )
mycursor=mydb.cursor()
sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
val=("Deepak","Berry Street")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
