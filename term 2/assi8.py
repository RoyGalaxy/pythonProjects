import mysql.connector as mycon
cn = mycon.connect(host='localhost',user='root',password="root",database="student",charset="utf8")
cur = cn.cursor()
print('Welcome to student Details Updation screen... ')

print("*******************EDIT STUDENT DETAILS **************************")
ro = int(input("Enter Student's roll number to edit :"))
query="select * from stud where roll="+str(ro)
cur.execute(query)
results = cur.fetchall()
if cur.rowcount<=0:
    print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
else:
    print("**************************************************")
    print('%5s'%"ROLL NO",'%15s'%'NAME','%12s'%'AGE','%10s'%'CLASS')
    print("**************************************************")
    for row in results:
        print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
print("-"*50)
ans = input("Are you sure to update ? (y/n)")
if ans=="y" or ans=="Y":
    d = input("Enter new name to update (enter old value if not to update) :")
    s = int(input("Enter new age to update (enter old value if not to update) :"))
    
    query="update stud set name='"+d+"',age="+str(s) + " where roll="+str(ro)
    
    cur.execute(query)
    cn.commit()
    print("\n## RECORD UPDATED  ##")    
