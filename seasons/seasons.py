from datetime import date
import re
import inflect

p = inflect.engine()

def main():
    date1 = input("Date of birth: ")
    if groups := re.search(r"^([0-9][0-9][0-9][0-9])-([0][1-9]|[1][0-2])-([0-2][0-9]|[3][0-1])$", date1):
        try:
            date2 = date(int(groups[1]), int(groups[2]), int(groups[3]))
        except ValueError:
            sys.exit("Invalid date")
        else:
            difference = date.today() - date2
            days = difference.days
            minutes = days * 24 * 60
            print(f"{p.number_to_words(minutes)} minutes")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
