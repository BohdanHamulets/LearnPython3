"""
File I/O
Reading a file -> .read()
Reading a line of a file - > .readline()
"""

whole_file = open("firstFile.bla", 'r')

print(str(whole_file.read()))

whole_file.close()

read_by_lines = open("firstFile.bla", 'r')

new_list = []

try:
    for x in range(5):
        new_list.append(read_by_lines.readline())
except:
    pass

read_by_lines.close()
print("Printing new_list : ", new_list)
