import re
# import sys


# def main():
#     print(convert(input("Hours: ")))


# def convert(s):
#     if times := re.search(r"(^[0-9]{1,2}(?::[0-9]{1,2})? (?:A|P)M) to ([0-9]{1,2}(?::[0-9]{1,2})? (?:A|P)M)", s):
#         print(times.group(1))
#         print(times.group(2))
#     else:
#         raise ValueError


# if __name__ == "__main__":
#     main()

s = input("Hours: ")
if times := re.search(r"(^[0-9]{1,2}(?::[0-9]{1,2})? (?:A|P)M) to ([0-9]{1,2}(?::[0-9]{1,2})? (?:A|P)M)", s):
    print(times.group(1))
    print(times.group(2))
else:
    print("False")
