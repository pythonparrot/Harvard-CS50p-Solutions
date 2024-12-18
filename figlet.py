from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    str = input("Input: ")
    figlet.setFont(font = random.choice(fonts))
    print(figlet.renderText(str))
elif len(sys.argv) == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in fonts:
        sys.exit()
    else:
        figlet.setFont(font = argv[2])
        str = input("Input: ")
        print(figlet.renderText(str))
else:
    sys.exit()


