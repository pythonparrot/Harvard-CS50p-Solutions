import sys
import requests

try:
    n = float(sys.argsv[1])
except IndexError:
    sys.exit("Missing command line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")


