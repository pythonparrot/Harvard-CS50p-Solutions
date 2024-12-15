def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    toReturn = d.replace("$", "")
    toReturn = float(toReturn)
    return toReturn


def percent_to_float(p):
    toReturn = p.replace("%", "")
    toReturn = float(toReturn)
    toReturn = toReturn / 100
    return toReturn


main()
