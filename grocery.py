groceries = {}

while True:
    try:
        item = input("Item: ").upper()
    except EOFError:
        break
    else:
        if item in groceries:
            groceries[item] += 1
        else:
            groceries.update({item: 1})

for item in sorted(groceries):
    print(groceries[item] + " " + item)

