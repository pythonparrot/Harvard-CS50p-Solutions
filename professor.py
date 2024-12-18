import random


def main():
    level = get_level()
    integer = generate_integer(level)
    print(str(integer))


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







