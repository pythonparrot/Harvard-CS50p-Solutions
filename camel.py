#Split the variable name based on upper cases
#Add the word together and put an underscore between each word
#Set everything to lower case
list = []
str = input("Variable name: ")
for i in range(len(str) - 1):
    if str[i].isupper():
        list.append(str[0, i - 1])
        str = str[i, len(str) - 1]
print(list)


