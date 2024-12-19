def has(string, letter):
    if string.lower().find(letter.lower()) >= 0:
        return True
    else:
        return False

def removeVowel(string, letter):
    string = string.replace(letter.upper(), "").replace(letter.lower(), "")
    return string

def main():
    string1 = input("Input: ")
    print(shorten(string1))

def shorten(word):
    if has(word, "a"):
        word = removeVowel(str, "a")
    if has(word, "e"):
        word = removeVowel(str, "e")
    if has (word, "i"):
        word = removeVowel(str, "i")
    if has (word, "o"):
        word = removeVowel(str, "o")
    if has (word, "u"):
        word = removeVowel(str, "u")
    return word

if __name__ == "__main__":
    main()
