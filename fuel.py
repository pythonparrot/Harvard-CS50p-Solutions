import sys

def main():
    frac = input("Fraction: ")
    print(convert(frac))



def convert(fraction):
    while True:
        x, y = fraction.split(sep = "/")
        x = float(x)
        y = float(y)
        if x <= y:
            if y != 0:
                num = (x/y)*100
                return gauge(num)
            else:
                raise ZeroDivisionError
        else:
            raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()

