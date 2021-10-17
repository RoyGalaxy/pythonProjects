import os
import platform
import mysql.connector

mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="root",\
                             database="student",charset="utf8")
print(mydb)
mycursor=mydb.cursor()

def removeStu():
    roll=int(input("Enter the roll number of the student to be deleted : "))
    rl=(roll,)
    sql="Delete from stud where roll=%s"
    mycursor.execute(sql,rl)
    print('Record deleted!!!')
    mydb.commit()
    
def stuview():
    mycursor.execute("select * from stud")
    myrus=mycursor.fetchall()
    for x in myrus:
        print(x)

def MenuSet(): #Function For The Student Management System
    print("Enter 1 : To Delete Student")
    print("Enter 2 : To View Students")
    userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    if(userInput == 1):
        removeStu()
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
 
