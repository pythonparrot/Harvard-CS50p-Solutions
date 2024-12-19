def main():
    while True:
    frac = input("Fraction: ")
    try:
        x, y = frac.split(sep = "/")
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
                    print(str(round(num * 100)) + "%")
                break

def convert(fraction):

def guage(percentage):

if __name__ == "__main__":
    main()

