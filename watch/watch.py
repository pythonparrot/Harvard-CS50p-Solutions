import re
# import sys


# def main():
#     print(parse(input("HTML: ")))


# def parse(s):
#     return re.fullmatch(r'src="(https?://(?:www\.)?youtube\.com/embed/\w+"', s)

# if __name__ == "__main__":
#     main()

input = input("HTML: ")
url = re.fullmatch(r'src="https?://(?:www\.)?(youtube\.com/embed/\w+)"', input)
print(url.group(1))

