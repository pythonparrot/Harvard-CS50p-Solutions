str = input("Input: ")

def has(string, letter):
    if string.lower().find(letter.lower()) >= 0:
        return true
    else:
        return false

def removeVowel(string, letter):
     string.find(letter.upper()) >= 0:
        string = string.remove(letter.upper())
    elif string.find(letter.lower()) >= 0:
        string = string.remove(letter.lower())


while has(str, "a") or has(str, "e") or has(str, "i") or has(str, "o") or has(str, "u"):
    if has(str, "a"):
        str = str.remove("A")
        str

print(str)

