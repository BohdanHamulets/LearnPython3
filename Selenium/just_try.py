import time


global i
i = 0

def wait():
    global i
    if i >= 10:
        print("Larger then 10, to be exact value is: ", i )

def sleep_then_add():
    global i
    time.sleep(2)
    i += 1
    print(i)


for x in range(10):
    sleep_then_add()

while True:
    time.sleep(2)
    wait()




