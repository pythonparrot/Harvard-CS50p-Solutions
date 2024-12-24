import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"([0-9][0-9]?[0-9]?):([0-9][0-9]?[0-9]?):([0-9][0-9]?[0-9]?):([0-9][0-9]?[0-9]?)", ip):
        for i in range(4):
            num = int(matches.group(i + 1))
            if num >= 0 and num <= 255:
                return "True"
            else:
                return "False"

if __name__ == "__main__":
    main()

