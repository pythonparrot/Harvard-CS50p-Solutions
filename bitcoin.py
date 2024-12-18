import sys
import requests

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get(https://api.coindesk.com/v1/bpi/currentprice.json).json()

except requests.RequestsException:
    sys.exit("Requests Error")

