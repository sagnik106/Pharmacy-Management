from flask import Flask, render_template,request, redirect
import mysql.connector

db=mysql.connector.connect(user='root',passwd='toor')
cursor=db.cursor()
cursor.execute("USE PHARMACY_MANAGEMENT")

app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        uid=request.form['username']
        pwd=request.form['password']
        try:
            cursor.execute('SELECT * FROM ADMINISTRATOR WHERE EMP_ID=\'%s\''%uid)
            c=0
            for t in cursor:
                c+=1;
            if c!=0:
                return redirect('admin')
            else:
                cursor.execute('SELECT * FROM MANAGER WHERE EMP_ID=\'%s\''%uid)
                c=0
                for t in cursor:
                    c+=1
                if c!=0:
                    return redirect('/manager')
                else:
                    cursor.execute('SELECT * FROM PHARMACIST WHERE EMP_ID=\'%s\''%uid)
                    c=0
                    for t in cursor:
                        c+=1
                    if c!=0:
                        return redirect('/pharmacist')
                    else:
                        return redirect('/')
        except:
            return redirect('/')
    else:
        return render_template('login.html')

@app.route('/admin',methods=['POST','GET'])
def admin():
    return render_template('admin.html')

@app.route('/manager',methods=['POST','GET'])
def manager():
    return render_template('manager.html')

@app.route('/pharmacist',methods=['POST','GET'])
def pharma():
    return render_template('pharmacy.html')

if __name__== '__main__':
    app.run(debug=True)