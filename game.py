import random

while True:
    level = input("Level: ")
    try:
        if isinstance(int(level), int) and level > 0:
            break
    except:
        

num = random.randint(1, level)

while True:
    guess = input("Guess: ")
    if guess < num:
        print("Too small!")
    if guess > num:
        print("Too large!")
    if guess == num:
        print("Just right!")
        break
