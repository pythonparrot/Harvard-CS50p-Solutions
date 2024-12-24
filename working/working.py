import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    times = re.search(r"[0-9]{1,2}()", s)

if __name__ == "__main__":
    main()
