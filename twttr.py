str = input("Input: ")

def has(string, letter):
    if string.lower().find(letter.lower()) >= 0:
        return true
    else:
        return false

while has(str, "a") or has(str, "e") or has(str, "i") or has(str, "o") or has(str, "u"):
    if has(str, "a"):
        str = str.remove

print(str)

