months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    try:
        date = input("Date: ").strip()
    except EOFError:
        break
    else:
        if date.count("/") == 2:
            month, day, year = date.split(sep = "/")
            if len(year) == 4 and (len(month) == 1 or len(month) == 2) and (len(day) == 1 or len(day) == 2) and int(day) <= 31 and int(day) >= 1 and int(month) >= 1 and int(month) <= 12:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
        elif date.count(" ") == 2:
            month, day, year = date.split()
            if int(day) <= 31 and int(day) >= 1 and int(month) >= 1 and int(month) <= 12:
                try:
                    month = months[month]
                except KeyError:
                    pass
                else:
                    day = day[0 : len(day) - 1]
                    print(f"{year}-{month}-{int(day):02}")
                    break




