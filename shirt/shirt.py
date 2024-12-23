import sys

if len(sys.argv) != 3:
    sys.exit("Not right amount of command line arguments.")
elif (not(sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")))
