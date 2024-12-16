#Split the variable name based on upper cases
str = input("Variable name: ")
list_indexes = []
for i in range(len(str)):
    if str[i].isupper():
        list_indexes.append(i)
list_words = []
for i in range list_indexes:
    if i == 0:
        list_words.append(str[0 : list_indexes[i]])
    if i == (len(list_indexes) - 1):
        list_words.append(str[list_indexes[i - 1] : list])


#Add the word together and put an underscore between each word
#Set everything to lower case



