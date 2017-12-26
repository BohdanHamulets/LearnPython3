"""
File I/O
Reading a file -> .read()
Reading a line of a file - > .readline()
"""

my_file = open("firstFile.bla", 'r')

#my_file.read()
#print(str(my_file.read()))

for object in my_file.read():
    print(object)

my_file.close()