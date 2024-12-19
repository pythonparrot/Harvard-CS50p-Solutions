import sys

def main():
    frac = input("Fraction: ")
    number = convert(frac)
    toPrint = gauge(number)
    print(toPrint)

def convert(fraction):
    while True:
        x, y = fraction.split(sep = "/")
        x = float(x)
        y = float(y)
        if y == 0:
            raise ZeroDivisionError
        else:
            if x <= y:
                num = round((x/y)*100)
                return num
            else:
                raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

