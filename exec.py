from flask import Flask, render_template,request
import mysql.connector

db=mysql.connector.connect(user='root',passwd='toor')
cursor=db.cursor()

app=Flask(__name__)

@app.route('/')
def login():
        return render_template('login.html')



if __name__== '__main__':
    app.run(debug=True)