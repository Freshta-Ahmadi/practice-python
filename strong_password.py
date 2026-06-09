import string


def check_password(password):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    check = f"{letters}{numbers}{symbols}"

    for i in password:
        if len(password) > 8 and i in check:
            print("strong password")
        elif len(password) < 8:
            if i in letters or numbers or symbols:
                print("weak password")
        else:
            print("medium password")


print("Check if your password is strong? ")

while True:
    user_password = input("Enter your password: ")
    check_password(user_password)
    choice = input("Do you want to check again: yes, no ").lower()
    if choice == "no":
        break

