import sys
import requests

try:
    n = int(sys.argsv[1])
except IndexError:
    sys.exit("Missing command line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

