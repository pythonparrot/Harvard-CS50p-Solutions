import pyfiglet
import sys
import random


figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:

elif len(sys.argv) == 3:
    if (argv[1] != "-f" and argv[1] != "--font") or argv[2] not in fonts:
        sys.exit()


