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
            time1_string2 = f"{groups1.group(1)}:00 {groups1.group(2)}"
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
            time2_string2 = f"{groups2.group(1)}:00 {groups2.group(2)}"
        #If time1_string2 is an PM time...
        if time1_string2.endswith("PM"):
            #... remove the " PM"
            time1_string2 = time1_string2.removesuffix(" PM")
            #Split up time1_string2 based on the colon
            x1, y1 = time1_string2.split(":")
            #Add 12 hours to the time
            x1 = str(int(x1) + 12)
            #Put the two numbers back together into a complete time
            time1_string2 = f"{x1}:{y1}"
        #Otherwise, if time1_string2 is an AM time...
        else:
            #... remove the " AM"
            time1_string2 = time1_string2.removesuffix(" AM")

        #If time2_string2 is a PM time...
        if time2_string2.endswith("PM"):
            #... remove the " PM"
            time2_string2 = time2_string2.removesuffix(" PM")
            #Split up time2_string2 based on the colon
            x2, y2 = time2_string2.split(":")
            #Add 12 hours to the time
            x2 = str(int(x2) + 12)
            #Put the two numbers back together into a complete time
            time2_string2 = f"{x2}:{y2}"
        #Otherwise, if time2_string2 is an AM time...
        else:
            #... remove the " AM"
            time2_string2 = time2_string2.removesuffix(" AM")

        if int(x1) < 10:
            time1_string2 = f"0{time1_string2}"
        if int(x2) < 10:
            time1_string2 = f"0{time2_string2}"
            
        #Finally, put the two final times together.
        return f"{time1_string2} to {time2_string2}"

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
