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
        word = removeVowel(word, "a")
    if has(word, "e"):
        word = removeVowel(word, "e")
    if has (word, "i"):
        word = removeVowel(word, "i")
    if has (word, "o"):
        word = removeVowel(word, "o")
    if has (word, "u"):
        word = removeVowel(word, "u")
    return word

if __name__ == "__main__":
    main()
