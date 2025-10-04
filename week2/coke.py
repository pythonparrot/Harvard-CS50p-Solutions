total = 0

while True:
    coin = int(input("Insert coin: "))
    if(coin == 25 or coin == 10 or coin == 5):
        total += coin
    if total < 50:
        print("Amount Due: " + str(50 - total))
    else:
        print("Change Owed: " + str(abs(50 - total)))
        break

