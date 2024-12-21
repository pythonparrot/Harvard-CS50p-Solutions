import sys

count = 0

if len(sys.argv) != 2:
    sys.exit("Error 1")
else:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.lstrip().startswith("#") != true and line.strip() != "":
                        count += 1
        except FileNotFoundError:
            sys.exit("Error 2")
    else:
        sys.exit("Error 3")
