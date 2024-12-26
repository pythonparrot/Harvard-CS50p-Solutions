from datetime import date
import re
import inflect


def main():
    date = input("Date of birth: ")
    if re.search(r"^[0-9][0-9][0-9][0-9]-(?:[0][1-9]|[1][0-2])-(?:[0-2][0-9]|[3][0-1])$", date)


if __name__ == "__main__":
    main()
