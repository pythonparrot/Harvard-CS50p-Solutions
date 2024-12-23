import sys

if len(sys.argv) != 3:
    sys.exit("Not exactly two command line arguments.")
else:
    try:
        with open(sys.argv[1], mode = "r") as file:
    except FileNotFoundError:
        sys.exit("File not found.")
    else:
        