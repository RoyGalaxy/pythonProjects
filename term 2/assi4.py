import os
import platform
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="student",charset="utf8")
print(mydb)
mycursor=mydb.cursor()

def stuInsert():
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    name=input("Enter the Name: ")
    L.append(name)
    age=int(input("Enter Age of Student : "))
    L.append(age)
    clas=input("Enter the Class : ")
    L.append(clas)
    
    stud=(L)
    sql="insert into stud (roll,name,age,clas) values (%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
def stuview():
    mycursor.execute("select * from stud")
    myrus=mycursor.fetchall()
    for x in myrus:
        print(x)

def MenuSet(): #Function For The Student Management System
    print("Enter 1 : To Add Student")
    print("Enter 2 : To View Students")
    userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    if(userInput == 1):
        stuInsert()
    if(userInput == 2):
        stuview()    
MenuSet()
def runAgain():
    runAgn = input("\nwant To Run Again Y/n: ")
    while(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
        runAgn = input("\nwant To Run Again y/n: ")
        
runAgain()
