import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Not exactly two command line arguments.")
else:
    try:
        with open(sys.argv[1], mode = "r") as bffile, open(sys.argv[2], mode = "w") as affile:
            bf_reader = csv.DictReader(file)
            af_writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            for row in bf_reader:
                last, first = row["name"].split(sep = ", ")
                for row1 in af_writer:
                    
    except FileNotFoundError:
        sys.exit("File not found.")
