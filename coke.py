total = 0

while True:
    total += int(input("Insert coin: "))
    if total < 50:
        print("Amount due: " + (50 - total))
    else:
        print("Change Owed: " + abs(50 - total))
        break

