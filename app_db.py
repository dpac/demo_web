from flask import Flask, redirect, url_for, request , render_template, jsonify
app = Flask(__name__)
import mysql.connector
mydb=mysql.connector.connect(
        host="10.0.3.165",
        user="admin",
        passwd="password",
        database="mydatabase"
        )

@app.route('/success/')
def success(name,com):
    mycursor=mydb.cursor()
    sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
    val=(name,com)
    mycursor.execute(sql,val)
    mydb.commit()
    return '1 row inserted'

@app.route('/show/')
def show():
    mycursor=mydb.cursor()
    sql="SELECT * FROM customers"
    mycursor.execute(sql)
    records=mycursor.fetchall()
    return jsonify(records)
    

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      nm = request.form['nm']
      cm  = request.form['cm']
      return success(nm,cm)

   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route("/insert")
def insert():
    return render_template('insert.html')

if __name__ == '__main__':
   app.run('0.0.0.0',debug = True)
