x, y, z = input("Expression: ").split()
x = float(x)
z = float(z)
match(y):
    case "+":
        print(round(x + z, 1))
    case "-":
        print(round(x - z, 1))
    case "*":
        print(round(x * z, 1))
    case _:
        print(round(x / z, 1))

