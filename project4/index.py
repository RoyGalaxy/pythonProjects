import pickle

# input user choice - search or add
task = input("What you want to do (search/add/exit): ");

if(task == "add"):
    data = [];

    while(True):
        rollNo = int(input("Enter student roll number: "))
        name = input("Enter student name: ")
        student = {"rollNo":rollNo,"name":name}

        data.append(student)
        addRes = input("want to add more students (y/n): ")

        if(addRes == "n"):
            break;
    
    file = open("students.dat","wb");
    pickle.dump(data,file);
    file.close()

elif(task == "search"):
    rollNo = int(input("Enter student's roll no, to be searched: "))
    
    file = open("students.dat","rb")
    record = pickle.load(file);
    file.close()
    for student in record:
        if(student["rollNo"] == rollNo):
            print(f"\nRecord found\nStudent Name: {student['name']}")
        else:
            print("No such record found!!!")

else:
    print("Thanks for using our project")
