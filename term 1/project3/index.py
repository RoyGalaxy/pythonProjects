f1 = open("file.txt")
f2 = open("newfile.txt","w")
for line in f1:
     if 'a' not in line:
          f2.write(line)

f1.close()
f2.close()

f2 = open("newfile.txt","r")
print(f2.read())