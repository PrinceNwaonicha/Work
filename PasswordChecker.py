import re

# Password requirements must be at least 8 char long
# Can contain any numbers, letters, and @#$%
# Ends with a number
pattern = re.compile(r"[\w@#$%]{8,}\d$")


def password_checker():
    while True:
        password = input(
            "Please input a password with at least 8 characters. \n You may use letter upper and lower, numbers and "
            "@#$%: ")
        check = pattern.search(password)
        if check is None:
            print("Sorry please enter a valid password")
        else:
            print(f"Thank you! Your secret password of {len(password) * '*'} has been recorded.")
            return password


password1 = password_checker()
print(password1)
