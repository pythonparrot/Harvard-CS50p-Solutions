#Split the variable name based on upper cases
str = input("Variable name: ")
words = []
start = 0

for i in range(len(str)):
    if str[i].isupper():
        words.append(str[start : i])
        start = i
    if i == len(str) - 1:
        words.append(str[start : len(str)])

finalStr = ""

for word in words:
    finalStr.append()

print(words)

#Add the word together and put an underscore between each word
#Set everything to lower case



