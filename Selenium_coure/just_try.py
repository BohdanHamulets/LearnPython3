import time

i = 0

def wait():
    global i
    if i >= 10:
        print("Larger then 10, to be exact value is: ", i )

def sleep_then_add():
    global i
    time.sleep(1)
    i += 1
    if i <= 10:
        print(i)
    else:
        pass

while True:
    sleep_then_add()
    wait()

print