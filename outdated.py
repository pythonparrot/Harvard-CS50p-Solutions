while True:
    try:
        date = input("Date: ")
    except EOFError:
        break
    else:
        if date.find("/") > 0 and date.count("/") == 2:
            x, y, z = date.split(sep = "/")
        elif date.find(" ") > 0:
            x, y, z = date.split()
