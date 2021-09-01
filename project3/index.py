# opening the file
file = open("file.txt","r");
# counting number of lines in the file
data = file.read();
dataArray = data.split("\n");
file.close();

# creating a second file
file2 = open("file2.txt","w");
# traversing through each line
for lineData in (dataArray):
    if('a' in lineData):
        file2.write(lineData + "\n");

file2.close()
print("Task omplete")