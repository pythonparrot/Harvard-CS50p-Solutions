import sys
import csv
import tabulate

if len(sys.argv) != 2:
    sys.exit("Not right amount of command line arguments.")
elif sys.argv[1].endswith(".csv") != True:
    sys.exit("Invalid file format.")
else:
    try:
        with open(sys.argv[1]) as file:
            to_tabulate = list(csv.reader(file))
            print(tabulate.tabulate(to_tabulate, tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("Specified file not found.")
