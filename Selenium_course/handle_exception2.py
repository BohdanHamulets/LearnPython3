"""
Exceptions are basically errors
"""

def ecxeptionHandler(argument):
    try:
        a = 10
        b = 20
        c = 0

        #d = ( a + b ) / c
        print(argument)
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    else:
        print("There was no exceptions")
    finally:
        print("I'm finally block, I always run ^_^")

ecxeptionHandler(5)
print("-+"*25)
ecxeptionHandler(3/0)