x, y, z = input("Expression: ").split()
x = float(x)
z = float(z)
x = round(x, 1)
z = round(z, 1)
match(y):
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case _:
        print(x / z)

