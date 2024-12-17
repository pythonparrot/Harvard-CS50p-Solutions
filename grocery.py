groceries = {

}

while True:
    try:
        item = input("").upper()
    except EOFError:
        break
    else:
        if item in groceries:
            groceries[item] += 1
        else:
            groceries.update({item: 1})

groceries = sorted(groceries)

for item in groceries:
    print(groceries[item] + " " + item)

