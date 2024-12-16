str = input("Variable name: ")
words = []
start = 0

for i in range(len(str)):
    if str[i].isupper():
        words.append(str[start : i])
        start = i
    if i == len(str) - 1:
        words.append(str[start : ])

finalStr = ""

for i in range(len(words)):
    if i == len(words) - 1:
        finalStr += words[i].lower()
    else:
        finalStr += words[i].lower() + "_"

print(finalStr)



