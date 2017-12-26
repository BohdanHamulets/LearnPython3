#
# Using With and As Methods - this makes .close() function deprecated - no need for it
#

print("With As Write Start")

with open("firstFile.bla", 'w') as with_as_write_object:
    with_as_write_object.write("This is and example of writing to file")

print()
print("With as Read Permission")
with open("firstFile.bla", 'r') as with_as_read_object:
    print(with_as_read_object.read())
