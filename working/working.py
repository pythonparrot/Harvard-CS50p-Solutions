import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if times := re.search(r"(^(?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M) to ((?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M)", s):
        time1_string1 = times.group(1)
        time2_string1 = times.group(2)
        if ":" in time1_string1:
            groups1 = re.search(r"^([1-9]|[1][0-2]):([0-5][0-9]) ((?:A|P)M)", time1_string1)
            time1_string2 = time1_string1
        else:
            groups1 = re.search(r"([1-9]) ((?:A|P)M)", time1_string1)
            time1_string2 = f"{groups1.group(1)}:00 {groups1.group(2)}

        if ":" in time2_string1:
            groups2 = re.search(r"^([1-9]|[1][0-2]):([0-5][0-9]) ((?:A|P)M)", time2_string1)
            time2_string2 = time2_string1
        else:
            groups2 = re.search(r"([1-9]) ((?:A|P)M)", time2_string1)
            time2_string2 = f"{groups2.group(1)}:00 {groups2.group(2)}

        if time1_string2.endwith("AM"):
            time1_string3 = time1_string2.removesuffix(" AM")
        else:
            time1_string3 = f"{str(int(groups1.group(1)) + 12)}:"


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
