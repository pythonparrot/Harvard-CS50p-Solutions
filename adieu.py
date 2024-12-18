import sys
import inflect

p = inflect.engine()

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        sys.exit(f"Adieu, adieu, to {p.join(names)}")

