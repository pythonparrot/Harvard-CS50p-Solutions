from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
fonts = figlet.getFonts()
str = input("Input: ")

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))
    print(figlet.renderText(str))
elif len(sys.argv) == 3:
    if (argv[1] != "-f" and argv[1] != "--font") or argv[2] not in fonts:
        sys.exit()
    else:
        figlet.setFont(font = argv[2])
        print(figlet.renderText(str))


