import sys
import csv
import tabulate

if len(sys.argv) != 2:
    sys.exit("Not right amount of command line arguments.")
elif sys.argv[1].endswith(".csv") != True
    sys.exit("Invalid file name format.")
else:
    try:
        with open(sys.argv[1]) as file:
            file = csv.reader(file)
            print(tabulate(file, tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("Specified file not found.")
