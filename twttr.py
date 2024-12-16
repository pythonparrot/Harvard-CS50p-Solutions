str = input("Input: ")
str1 = str.lower()

while True:
    if str1.find("a") != -1:
        i = str1.find("a")
        str = str[0 : i] + str[i + 1 : ]
        str1 = str[0 : i] + str[i + 1 : ]
    elif str1.find("e") != -1:
        i = str1.find("e")
        str = str[0 : i] + str[i + 1 : ]
        str1 = str[0 : i] + str[i + 1 : ]
    elif str1.find("i") != -1:
        i = str1.find("i")
        str = str[0 : i] + str[i + 1 : ]
        str1 = str[0 : i] + str[i + 1 : ]
    elif str1.find("o") != -1:
        i = str1.find("o")
        str = str[0 : i] + str[i + 1 : ]
        str1 = str[0 : i] + str[i + 1 : ]
    elif str1.find("u") != -1:
        i = str1.find("u")
        str = str[0 : i] + str[i + 1 : ]
        str1 = str[0 : i] + str[i + 1 : ]
    else:
        break

print(str)

