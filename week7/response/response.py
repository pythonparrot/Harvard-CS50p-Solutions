import validators

email1 = input("What's your email address?: ")
try:
    if validators.email(email1):
        print("Valid")
    else:
        print("Invalid")
except ValidationError:
    print("Invalid")
