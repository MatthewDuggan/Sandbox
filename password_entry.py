"""Matthew Duggan"""

password = input("input your password: ")
MIN_LENGTH = 10
if len(password) >= MIN_LENGTH:
    for char in password:
        print("*",end="")
else:
    print("The password is shorter than the required length")

