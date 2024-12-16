def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0 : 2].isalpha():
            if s.isalnum():
                index = 0
                for i in range(len(s)):
                    if s[i].isdigit():
                        index = i
                        break
                for i in range(index + 1, len(s)):
                    bool = True
                    if s[i].isalpha():
                        bool = False
                        break
                if bool == True:
                    return True

    return False

main()
