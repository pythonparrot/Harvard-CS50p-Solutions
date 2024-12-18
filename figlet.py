from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    user_input = input("Input: ")
    figlet.setFont(font = random.choice(fonts))
    print(figlet.renderText(user_input))
elif len(sys.argv) == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in fonts:
        sys.exit()
    else:
        figlet.setFont(font = sys.argv[2])
        user_input = input("Input: ")
        print(figlet.renderText(user_input))
else:
    sys.exit()


