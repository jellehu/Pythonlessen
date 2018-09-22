import re

newpassword = input("Voer uw nieuwe wachtwoord in: ")

def hasDigit(input):
    return bool(re.search(r'\d', input))

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) > 6 and hasDigit(newpassword) == 1:
        return True
    else:
        return False

print(new_password("wachtwoord1", newpassword))