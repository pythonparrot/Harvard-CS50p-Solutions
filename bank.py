g = input("Greeting: ").lower().strip()
if g.find("hello") == 0:
    print("$0")
elif g.find("h") == 0:
    print("$20")
else:
    print("$100")
