import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        for i in range(10):
            if n == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                
            if n == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
            if n == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)




