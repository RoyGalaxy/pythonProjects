# opening a file and reading the data
file = open("file.txt","r");
data = file.read()
file.close();

characters = 0
numbers = 0
spaces = 0
# traversing through the data string
for i in data:
    if(i.isspace()):
        spaces = spaces + 1;
    if(i.isdigit()):
        numbers = numbers + 1
    if(i.isalpha()):
        characters = characters + 1

print(f"characters:{characters}, numbers:{numbers}, spaces:{spaces}")