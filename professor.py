import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n == 1:
            x, y = random.randint(0, 9)


