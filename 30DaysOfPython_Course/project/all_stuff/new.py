items = ["ada", "blabla", 357, "Debian", 
777, 741.25, "Irvin",]

string_items = []
int_items = []

for x in items:
    if isinstance(x, float) or isinstance(x, int):
        int_items.append(x)
    elif isinstance(x, str):
        string_items.append(x)
    else:
        pass

print(string_items)
print(int_items)
print("This was a for loop")

def parse_list(some_list):
    list_with_string = []
    list_with_integers = []
    for x in some_list:
        if isinstance(x, float) or isinstance(x, int):
            list_with_string.append(x)
        elif isinstance(x, str):
            list_with_integers.append(x)
        else:
            pass
    #return list_with_string + list_with_integers

newbie = parse_list(items)
print(newbie)
print("this was a function")
#print(parse_list(items))


def count_lenth_of_list(argument):
    len(argument)
    #return count_lenth_of_list(argument)

var_for_conunt_result = count_lenth_of_list(items)
print("This was Lenth (len) function")
