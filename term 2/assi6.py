import os
import platform
import mysql.connector

mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="root",\
                             database="student",charset="utf8")
print(mydb)
mycursor=mydb.cursor()

def stuview():
    print("Select the search criteria : ")
    print("1. Roll")
    print("2. Name")
    print("3. Age")
    print("4. Class")
    print("5. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter roll no : "))
        rl=(s,)
        sql="select * from stud where roll=%s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from stud where name=%s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input("Enter age : "))
        rl=(s,)
        sql="select * from stud where age=%s"
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input("Enter Class : ")
        rl=(s,)
        sql="select * from stud where clas=%s"
        mycursor.execute(sql,rl)
    elif ch==5:
        sql="select * from stud"
        mycursor.execute(sql)   
    res=mycursor.fetchall()
    print("The Students details are as follows : ")
    print("(ROll, Name, Age, Class)")
    for x in res:
        print(x)

def MenuSet(): #Function For The Student Management System
    print("Enter 1 : To Search Student")
    userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    if(userInput == 1):
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
