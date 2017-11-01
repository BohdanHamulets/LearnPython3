import random

list_for_random = ["go_on", "don't be scared", "continue", "stop",]
list_for_random2 = ["go_on", "don't be scared", "continue", 1 , 2, 3, 4, 4, 5, 5, "stop", "go ahead", "don't stop", ]

def rekyrsia(list_of_actions):
    what_was_it = random.choice(list_of_actions)
    if  what_was_it == "stop":
        print("choise was to stop")
    else:
        x = 0
        x =+1
        print("Choise was", what_was_it)
        rekyrsia(list_of_actions)

rekyrsia(list_for_random2)
