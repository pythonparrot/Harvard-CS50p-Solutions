months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        date = input("Date: ")
    except EOFError:
        break
    else:
        if date.find("/") > 0 and date.count("/") == 2:
            month, day, year = date.split(sep = "/")
            if len(year) == 4 and (len(month) == 1 or len(month) == 2) and (len(day) == 1 or len(day) == 2):
                date = 

        elif date.find(" ") > 0 and date.count(" ") == 2:
            month, day, year = date.split()

