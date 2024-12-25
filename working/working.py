import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #Checks that format is correct and times are valid
    if times := re.search(r"(^(?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M) to ((?:[1-9]|[1][0-2])(?::[0-5][0-9])? (?:A|P)M)", s):
        #Assigns first time (e.g., 9:00 AM) to time1_string1
        time1_string1 = times.group(1)
        #Assigns second time (e.g, 5:00 PM) to time2_string1
        time2_string1 = times.group(2)
        #If there is a colon in the first time...
        if ":" in time1_string1:
            #... assigns 3 "groups" into groups1, being the number before the colon, the number after the colon, and the AM/PM.
            groups1 = re.search(r"^([1-9]|[1][0-2]):([0-5][0-9]) ((?:A|P)M)", time1_string1)
            #Assigns time1_string1 to time1_string2 because no further changes need to be made for now.
            time1_string2 = time1_string1
        #Otherwise, since there isn't a colon in the first time...
        else:
            #... assigns 2 "groups" into groups1, being the number and the AM/PM.
            groups1 = re.search(r"([1-9]) ((?:A|P)M)", time1_string1)
            #Adds a :00 to the end of the number and assigns it to time1_string2.
            time1_string2 = f"{groups1.group(1)}:00 {groups1.group(2)}
        #If there is a colon in the second time...
        if ":" in time2_string1:
            #... assigns 3 "groups" into groups2, being the number before the colon, the number after the colon, and the AM/PM.
            groups2 = re.search(r"^([1-9]|[1][0-2]):([0-5][0-9]) ((?:A|P)M)", time2_string1)
            #Assigns time2_string1 to time2_string2 because no further changes need to be made for now.
            time2_string2 = time2_string1
        #Otherwise, since there isn't a colon in the second time...
        else:
            #... assigns 2 "groups" into groups2, being the number and the AM/PM.
            groups2 = re.search(r"([1-9]) ((?:A|P)M)", time2_string1)
            #Adds a :00 to the end of the number and assigns it to time2_string2.
            time2_string2 = f"{groups2.group(1)}:00 {groups2.group(2)}
        #If time1_string2 is an AM time...
        if time1_string2.endwith("AM"):
            #Add 12 hours to the time, remove the " AM", and set it equal to time1_string3.
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
