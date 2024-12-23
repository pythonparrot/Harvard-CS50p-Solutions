import sys
from PIL import Image
from PIL import ImageOps
import os



if len(sys.argv) != 3:
    sys.exit("Invalid amount of command line arguments.")
elif (not sys.argv[1].lower().endswith(".jpg", ".jpeg", ".png")) or (not sys.argv[2].lower().endswith(".jpg", ".jpeg", ".png")):
    sys.exit("Invalid file(s) format.")

extension1 = os.path.splittext(sys.argv[1])[1].lower()
extension2 = os.path.splittext(sys.argv[2])[1].lower()
if extension1 != extension2:
    sys.exit("Input extension doesn't match output extension.")
else:
    try:
        input_pic = Image.open(sys.argv[1])
        shirt_pic = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("File not found.")
    else:
        size = shirt_pic.size
        resized_input_pic = ImageOps.fit(input_pic, size)
        resized_input_pic.paste(shirt_pic, shirt_pic)
        resized_input_pic.save(sys.argv[2])



