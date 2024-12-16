x, y, z = input("Expression: ").split()
x = float(x, 1)
z = float(z, 1)
match(y):
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case _:
        print(x / z)

