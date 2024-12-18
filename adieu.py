import sys

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        sys.exit()
    else:
        

