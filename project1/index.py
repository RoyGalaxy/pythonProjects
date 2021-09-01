# opening text file and reading the data
file = open("file.txt","r");
data = file.read();
file.close();

# manipulating data and printing it
output_data = data.replace(" "," #")
print(output_data)