"""
File I/0
'w' -> Write Only Mode
'r' -> Read Only Mode
'r+' -> Read and Write Mode
'a' -> Append Only Mode
"""
import os

my_list = ["1 line", "2 line", "3 line"]

filename = "firstFile.bla"
path = os.getcwd() + '/' + filename
my_file = open(path, "w")

for item in my_list:
    my_file.write(str(item) + '\n')

# my_file.close()

path_ = os.getcwd()
print(path)