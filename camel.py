#Split the variable name based on upper cases
str = input("Variable name: ")
words = []
start = 0

for i in range(len(str)):
    if str[i].isupper():
        words.append(str[start : i])
        start = i

print(words)

#Add the word together and put an underscore between each word
#Set everything to lower case



