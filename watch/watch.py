import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url_ending = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"', s)
    new_url = f"https://youtu.be/{url_ending.group(1)}"
    return new_url

if __name__ == "__main__":
    main()
