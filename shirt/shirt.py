import sys
import Pillow

if len(sys.argv) != 3:
    sys.exit("Invalid amount of command line arguments.")
elif (not sys.argv[1].lower().endswith(".jpg", ".jpeg", ".png")) or (not sys.argv[2].lower().endswith(".jpg", ".jpeg", ".png")):
    sys.exit("Invalid file(s) format.")
elif sys.argv[1][-2:] != sys.argv[2][-2:]:
    sys.exit("Input extension doesn't match output extension.")
else:
    try:
        
    except FileNotFoundError:
        sys.exit("File not found.")
