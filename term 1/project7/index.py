import csv
def writeRecord(data):
    with open("users.csv","a",newline="") as myfile:
        writer = csv.writer(myfile)
        writer.writerow(data)
def readRecord():
    with open("users.csv","r") as myfile:
        reader = csv.reader(myfile)
        print("----Display Record-----")
        for row in reader:
            print(f"\nUser   Password")
            print(f"{row[0]}   {row[1]}\n")
def Search(uid):
    with open("users.csv","r") as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            if row[0] == uid:
                print(f"userId: {row[0]}\nPassword: {row[1]}")
def Input():
    n = int(input("How many records you want to enter: "))
    for i in range(n):
        uid = input("Enter user id: ")
        upass = input("Enter password: ")
        writeRecord([uid,upass])
def main():
    while True:
        print("1.Insert user")
        print("2.Display users")
        print("3.Search password (by user id)")
        print("0.Exit")
        ch = int(input("Enter your choice: "))
        if(ch == 1):
            Input()
        elif(ch == 2):
            readRecord()
        elif(ch == 3):
            uid = input("Enter user id to be searched: ")
            Search(uid)
        elif(ch == 0):
            break
main()