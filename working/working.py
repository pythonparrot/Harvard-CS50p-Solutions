import re
# import sys


# def main():
#     print(convert(input("Hours: ")))


# def convert(s):
#     if times := re.search(r"^[0-9]{1,2}(?::00)? (?:A|P)M to [0-9]{1,2}(?::00)? (?:A|P)M", s)

#     else:
#         raise ValueError


# if __name__ == "__main__":
#     main()

s = input("Hours: ")
if re.search(r"^[0-9]{1,2}(?::[0-9]{1,2})? (?:A|P)M to [0-9]{1,2}(?::[0-9]{1,2})? (?:A|P)M", s):
    print("True")
else:
    print("False")
