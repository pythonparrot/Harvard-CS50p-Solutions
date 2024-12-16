#Split the variable name based on upper cases
str = input("Variable name: ")
list_indexes = []
for i in range(len(str)):
    if str[i].isupper():
        list_indexes.append(i)

print(list_indexes)

list_words = []

for i in range(len(list_indexes)):
    if i == 0:
        list_words.append(str[0 : list_indexes[i]])
    if i == (len(list_indexes) - 1):
        list_words.append(str[list_indexes[i]])
    else:
        list_words.append(str[list_indexes[i - 1] : list_indexes[i]])

print(list_words)

#Add the word together and put an underscore between each word
#Set everything to lower case



