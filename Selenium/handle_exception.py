def universal_bad_code(smth):
    try:
        # so here, if we don't put raise keyword - "Process finished with exit code 0"
        # and if we actually want to see those exceptions work - we need to put it
        raise smth
    except TypeError:
        a = 0
        a += 1
        print("There was an TypeError, it will be logged, rest of the code will be executed", a)
    except ZeroDivisionError:
        b = 0
        b += 1
        print("There was an ZeroDivisionError, it will be logged, rest of the code will be executed", b)
    except IndexError:
        c = 0
        c += 1
        return("There was an IndexError, it will be logged, rest of the code will be executed", c)
    #print("Outside of exception block")

def zero_division():
    a = 7
    b = 0
    a / b


def type_error():
    b = 'o'
    z = 7
    b / z


def index_error():
    superlist= ['a', 'b', 'c']
    superlist[7]

universal_bad_code(zero_division)
universal_bad_code(type_error)
universal_bad_code(index_error)