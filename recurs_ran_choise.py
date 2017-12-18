import random

list_for_random = ["go_on", "don't be scared", "continue", "keep going", "proceed", "go again", "stop",]

def rekyrsia(list_of_actions):
    x = 0
    what_was_it = random.choice(list_of_actions)
    if  what_was_it == "stop":
        print("choice was to stop")
    else:
        x =+1
        print('"Choise was -', what_was_it,'"')
        rekyrsia(list_of_actions)

rekyrsia(list_for_random)
