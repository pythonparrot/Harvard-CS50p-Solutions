import sys
import inflect

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        sys.exit()
    else:
        print(f"Adieu, adieu, to {inflect.join(names)}")

