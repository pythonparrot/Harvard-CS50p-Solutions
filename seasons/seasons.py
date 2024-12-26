from datetime import date
import re
import inflect


def main():
    date1 = input("Date of birth: ")
    if groups := re.search(r"^([0-9][0-9][0-9][0-9])-([0][1-9]|[1][0-2])-([0-2][0-9]|[3][0-1])$", date1):
        try:
            date2 = date(groups[1], groups[2], groups[3])
        except ValueError:
            sys.exit("Invalid date")
        else:
            difference = date.today() - date2
            
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
