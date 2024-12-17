menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.00

while True:
    try:
        item = input("Item: ").title()
    except EOFError:
        break
    else:
        try:
            price = menu[item]
        except KeyError:
            pass
        else:
            price = float(menu[item])
            total += price
            if (total * 100) % 10 == 0:
                print(f"Total: ${total}0")
            else:
                print(f"Total: ${total}")




