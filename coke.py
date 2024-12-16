total = 0

while True:
    total += int(input("Insert coin: "))
    if total < 50:
        print("Amount Due: " + str(50 - total))
    else:
        print("Change Owed: " + str(abs(50 - total)))
        break

