#import input

number = int(input("Enter your number here >>"))

def checkio(number):
    
    if isinstance(number, float) or isinstance(number, int):
        if (number % 5 == 0) and (number % 3 == 0):
            return("Fizz Buzz")
        elif (number % 3 == 0):
             return("Fizz")
        elif (number % 5 == 0):
            return("Buzz")
        else:
            return("Your number is not divisible by 3 or 5")
    else:
        return("""Value that you've entered is not integer or float or even a sting with a value that can be converted to one!\n
What is wrong with you?""")


print(checkio(number))
#print(checkio(20))
#print(checkio(15))
#print(checkio(5))
#print(checkio(3.#7))
#print(checkio("bla"))


	