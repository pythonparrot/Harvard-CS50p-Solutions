def main():
    time = input("What time is it? ")
    time = convert(time)
    if (time >= 7 and time <= 8)


def convert(time):
    x, y = time.split(sep = ":")
    y = float(y)/60
    return x + y

if __name__ == "__main__":
    main()
