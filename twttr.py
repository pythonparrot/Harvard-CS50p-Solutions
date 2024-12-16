def has(string, letter):
    if string.lower().find(letter.lower()) >= 0:
        return True
    else:
        return False

def removeVowel(string, letter):
    string = string.replace(letter.upper(), "").replace(letter.lower(), "")
    return string

def main():
    str = input("Input: ")

    if has(str, "a"):
        str = removeVowel(str, "a")
    if has(str, "e"):
        str = removeVowel(str, "e")
    if has (str, "i"):
        str = removeVowel(str, "i")
    if has (str, "o"):
        str = removeVowel(str, "o")
    if has (str, "u"):
        str = removeVowel(str, "u")

    print(str)

main()
