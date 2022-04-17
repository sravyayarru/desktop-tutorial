# writing data into a file
file=open('c:\demofile\myfile.txt','w')
file.write("THIS IS MY FIRST FILE \n")
file.write("THIS IS MY SECOND FILE \n")
file.close()

# reading data from the file
file=open('c:\demofile\myfile.txt','r')
print(file.read())
file.close()

file=open('c:\demofile\myfile.txt','r')
print(file.read(10)) #read given number of characters from as file
file.close()

file=open('c:\demofile\myfile.txt','r')
print(file.readlines()) #read entire content of file at once in array format
file.close()

file=open('c:\demofile\myfile.txt','r')
print(file.readline()) #read first line
file.close()

# appending data
file=open('c:\demofile\myfile.txt','a')
file.write('THIS IS  MY THIRD LINE \n')
file.close()

# looping through the data using for loop
file=open('c:\demofile\myfile.txt','r')
for line in file:
    print(line)
file.close()

