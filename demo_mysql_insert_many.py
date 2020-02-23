import mysql.connector

mydb=mysql.connector.connect(
        host="webdemo.cbkr1mai5bui.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        passwd="cisco123",
        database="mydatabase"
        )
mycursor=mydb.cursor()
sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
val=[("Priyanka","Berry Street"),
     ("Amy","Dorris Street"),
     ("Michael","Miller Street"),
     ("Chris","Pacific Highway"),
     ("Adam","Park Street")
        
        ]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
