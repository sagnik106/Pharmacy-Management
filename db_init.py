import mysql.connector

db = mysql.connector.connect(user="root",passwd="toor")
cursor=db.cursor()
def initialize():
    cursor.execute('CREATE DATABASE PHARMACY_MANAGEMENT')
    cursor.execute('USE PHARMACY_MANAGEMENT')
    cursor.execute('CREATE TABLE ADMINISTRATOR(PASSWORD VARCHAR(15),EMP_ID INT PRIMARY KEY)')
    cursor.execute('CREATE TABLE MANAGER(PASSWORD VARCHAR(15), EMP_ID INT PRIMARY KEY)')
    cursor.execute('CREATE TABLE PHARMACIST(PASSWORD VARCHAR(15),EMP_ID INT PRIMARY KEY)')
    cursor.execute('CREATE TABLE EMPLOYEE(F_NAME VARCHAR(10) NOT NULL, L_NAME VARCHAR(10), EMP_ID INT PRIMARY KEY, EMAIL VARCHAR(20), PHONE VARCHAR(10), DOB VARCHAR(10))')
    cursor.execute('CREATE TABLE PRESCRIPTION(PRES_ID INT NOT NULL, QUANTITY INT, DOSE INT, D_NAME VARCHAR(10))')
    cursor.execute('CREATE TABLE INVOICE(C_NAME VARCHAR(30), PRES_ID INT NOT NULL, EMP_ID INT, IDATE VARCHAR(10), PRICE FLOAT)')
    cursor.execute('CREATE TABLE STOCK(D_NAME VARCHAR(10),QUANTITY INT, COST FLOAT, SUPPLIER VARCHAR(10))')
    cursor.execute(r"INSERT INTO ADMINISTRATOR VALUES('toor',1000)")
    cursor.execute(r"INSERT INTO EMPLOYEE(F_NAME,EMP_ID) VALUES('root',1000)")
    db.commit()
initialize()