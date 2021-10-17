myfile = open("file.txt",'r')
for  line in myfile:
     word= line .split()
     for w in word:
          print(w + '#',end ='')
     print()
myfile.close()