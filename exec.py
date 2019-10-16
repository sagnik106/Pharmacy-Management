from flask import Flask, render_template,request, redirect
import mysql.connector

db=mysql.connector.connect(user='root',passwd='toor')
cursor=db.cursor(buffered=True)
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

@app.route('/prescripa',methods=['POST','GET'])
def prescripa():
    if request.method=='POST':
        cname=request.form[cname]
        eid=request.form[eid]
        pid = request.form[pid]
        dname = request.form[dname]
        quantity = request.form[quantity]
        dose = request.form[dose]
        price=request.form[price]
        date=request.form[date]
        cursor.execute(r"INSERT INTO PRESCRIPTION VALUES(%ld,%ld,%ld,'%s')" % (pid, quantity, dose, dname))
        cursor.execute(r"INSERT INTO INVOICE VALUES('%s',%ld,%ld,'%s',%f)" % (cname, pid, eid, date, price))
        db.commit()
        cursor.close()
        return redirect("/admin")
    else:
        return render_template('prescripa.html')

@app.route('/prescripp',methods=['POST','GET'])
def prescripp():
    if request.method == 'POST':
        cname = request.form[cname]
        eid = request.form[eid]
        pid = request.form[pid]
        dname = request.form[dname]
        quantity = request.form[quantity]
        dose = request.form[dose]
        price = request.form[price]
        date = request.form[date]
        cursor.execute("INSERT INTO PRESCRIPTION VALUES(%ld,%ld,%ld,\'%s\')" % (pid, quantity, dose, dname))
        cursor.execute("INSERT INTO INVOICE VALUES(\'%s\',%ld,%ld,\'%s\',%f)" % (cname, pid, eid, date, price))
        db.commit()
        cursor.close()
        return redirect("/pharmacist")
    else:
        return render_template('prescripp.html')

@app.route('/inva',methods=['POST','GET'])
def inva():
    cursor.execute('SELECT * FROM INVOICE')
    tasks=cursor.fetchall()
    return render_template('inva.html',tasks=tasks)

@app.route('/invp',methods=['POST','GET'])
def invp():
    cursor.execute('SELECT * FROM INVOICE')
    tasks = cursor.fetchall()
    return render_template('invp.html', tasks=tasks)

@app.route('/stockm',methods=['POST','GET'])
def stockm():
    cursor.execute('SELECT * FROM STOCK')
    tasks = cursor.fetchall()
    return render_template('stockm.html', tasks=tasks)

@app.route('/stocka',methods=['POST','GET'])
def stocka():
    cursor.execute('SELECT * FROM STOCK')
    tasks = cursor.fetchall()
    return render_template('stocka.html',tasks=tasks)

@app.route('/empa',methods=['POST','GET'])
def empa():
    cursor.execute('SELECT * FROM EMPLOYEE')
    tasks=cursor.fetchall()
    return render_template('empa.html',tasks=tasks)

@app.route('/empm',methods=['POST','GET'])
def empm():
    cursor.execute('SELECT * FROM EMPLOYEE')
    tasks=cursor.fetchall()
    return render_template('empm.html',tasks=tasks)

@app.route('/upstockm/<int:cost>',methods=['POST','GET'])
def upstockm(cost):
    if request.method == 'POST':
        num=request.form[num]
        cursor.execute(r"UPDATE STOCK SET QUANTITY = %d WHERE COST = %d"%(num,cost))
        db.commit()
        cursor.close()
        return redirect('/stockm')
    else:
        return render_template('/upstockm')

@app.route('/upstocka/<int:cost>',methods=['POST','GET'])
def upstocka(cost):
    if request.method == 'POST':
        num=request.form[num]
        cursor.execute(r"UPDATE STOCK SET QUANTITY = %d WHERE COST = %d"%(num,cost))
        db.commit()
        cursor.close()
        return redirect('/stocka')
    else:
        return render_template('/upstocka')

@app.route('/delstockm/<int:cost>',methods=['POST','GET'])
def delstockm(cost):
    cursor.execute(r"DELETE FROM STOCK WHERE COST=%d"%(cost))
    db.commit()
    cursor.close()
    return redirect('/stockm')

@app.route('/delstocka/<int:cost>',methods=['POST','GET'])
def delstocka(cost):
    cursor.execute(r"DELETE FROM STOCK WHERE COST=%d"%(cost))
    db.commit()
    cursor.close()
    return redirect('/stocka')

@app.route('/delempm/<int:eid>', methods=['POST', 'GET'])
def delempkm(eid):
    cursor.execute(r"DELETE FROM STOCK WHERE EMP_ID=%d" % (eid))
    db.commit()
    cursor.close()
    return redirect('/empm')


@app.route('/delempa/<int:eid>', methods=['POST', 'GET'])
def delempa(eid):
    cursor.execute(r"DELETE FROM EMPLOYEE WHERE EMP_ID=%d" % (eid))
    db.commit()
    cursor.close()
    return redirect('/empa')

@app.route('/addemp',methods=['POST','GET'])
def addemp():
    if request.method == 'POST':
        fname=request.form[fname]
        lname=request.form[lname]
        eid=request.form[eid]
        mail=request.form[mail]
        ph=request.form[ph]
        dob=request.form[dob]
        cursor.execute(r"INSERT INTO EMPLOYEE VALUES('%s','%s',%d,'%s','%s','%s')"%(fname,lname,eid,mail,ph,dob))
        db.commit()
        cursor.close()
        return redirect('/empa')
    else:
        return render_template('empform.html')

@app.route('/addstock',methods=['POST','GET'])
def addstock():
    if request.method == 'POST':
        dname=request.form[dname]
        quantity=request.form[quantity]
        cost=request.form[cost]
        sup=request.form[sup]
        cursor.execute(r"INSERT INTO STOCK VALUES('%s',%d,%f,'%s')"%(dname,quantity,cost,sup))
        db.commit()
        cursor.close()
        return redirect('/stocka')
    else:
        return render_template('stockform.html')

if __name__== '__main__':
    app.run(debug=True)