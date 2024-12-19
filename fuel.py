def main():
    while True:
        frac = input("Fraction: ")
        convert(frac)


def convert(fraction):
    try:
        x, y = fraction.split(sep = "/")
        x = float(x)
        y = float(y)
    except ValueError:
        pass
    else:
        if x.is_integer() and y.is_integer() and x <= y:
            try:
                num = x/y
            except ZeroDivisionError:
                pass
            else:
                if num <= 0.01:
                    print("E")
                elif num >= 0.99:
                    print("F")
                else:
                    return str(round(num * 100)) + "%"
                break

def guage(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

