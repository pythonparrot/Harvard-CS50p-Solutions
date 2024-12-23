import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) != 3:
    sys.exit("Invalid amount of command line arguments.")
elif (not sys.argv[1].lower().endswith(".jpg", ".jpeg", ".png")) or (not sys.argv[2].lower().endswith(".jpg", ".jpeg", ".png")):
    sys.exit("Invalid file(s) format.")
elif sys.argv[1][-2:] != sys.argv[2][-2:]:
    sys.exit("Input extension doesn't match output extension.")
else:
    try:
        pic1 = Image.open(sys.argv[1])
        pic2 = Image.open(sys.argv[2])
        shirt_pic = 
    except FileNotFoundError:
        sys.exit("File not found.")
    else:
        size = "shirt.png".size
        resized_pic1 = ImageOps.fit(pic1, size))


