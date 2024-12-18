import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        count = 0
        problem = f"{x} + {y} = "
        while count < 3:
            try:
                answer = int(input(problem))
            except ValueError:
                print("EEE")
                count += 1
            else:
                if answer == sum:
                    score += 1
                    break
                else:
                    print("EEE")
                    count += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            break
        except ValueError:
            pass
    return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()







