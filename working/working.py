import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if times := re.search(r"(^(?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M) to ((?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M)", s):
        time1_string1 = times.group(1)
        time2_string1 = times.group(2)
        if time1_string1.endswith("AM"):
            
    else:
        raise ValueError


if __name__ == "__main__":
    main()

# s = input("Hours: ")
# if times := re.search(r"(^(?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M) to ((?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M)", s):
#     print(times.group(1))
#     print(times.group(2))
# else:
#     print("False")
