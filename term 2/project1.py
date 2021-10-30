import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger",database="gvkcv")
if mycon.is_connected()==False:
    print("error connecting to database")
cursor=mycon.cursor()
cursor.execute("select *from student10")
data=cursor.fetchall()
for i in data:
    print(i)
mycon.close()