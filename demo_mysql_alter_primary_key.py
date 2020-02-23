import mysql.connector

mydb=mysql.connector.connect(
        host="webdemo.cbkr1mai5bui.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        passwd="cisco123",
        database="mydatabase"
        )
mycursor=mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
