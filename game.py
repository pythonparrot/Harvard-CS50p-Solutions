import random

while True:
    level = input("Level: ")
    try:
        if isinstance(int(level), int) and int(level) > 0:
            break
    except ValueError:
        pass

num = random.randint(1, int(level))

while True:
    try:
        guess = int(input("Guess: "))
        if guess < num:
            print("Too small!")
        if guess > num:
            print("Too large!")
        if guess == num:
            print("Just right!")
            break
    except ValueError:
        pass
