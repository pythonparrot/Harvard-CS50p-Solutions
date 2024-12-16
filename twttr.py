str = input("Input: ")

def has(string, letter):
    if string.lower().find(letter.lower()) >= 0:
        return true
    else:
        return false

def removeVowel(string, letter):
    while string.find(letter.upper()) >= 0:
        string = string.remove(letter.upper())
    while string.find(letter.lower()) >= 0:
        string = string.remove(letter.lower())
    return string


def main():
    if has(str, "a"):
        removeVowel(str, "a")
    if has(str, "e"):
        removeVowel(str, "e")
    if has (str, "i")

