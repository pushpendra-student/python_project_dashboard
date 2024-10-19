import random
import string

def generate_password(min_lenght , number = True,special_character = True):
    letters = string.ascii_letters
    digits = string.digits
    special =  string.punctuation
    
    character = letters
    if number:
        character += digits
    if special_character:
        character += special


    pwd = ""
    has_number = False
    has_special = False
    meets_critiria = False

    while not meets_critiria or len(pwd)<min_lenght:
        new_pwd = random.choice(character)
        pwd += new_pwd

        if new_pwd in digits:
            has_number = True

        if new_pwd in special:
            has_special = True

        meets_critiria = True

        if number:
            meets_critiria = has_number
        if special_character:
            meets_critiria = meets_critiria and has_special

    return pwd


numbers = input("Do you want number in password (y/n): ").lower() =="y"
symbols = input("Do you want character in your password (y/n): ").lower() =="y"

password = generate_password(10 ,numbers , symbols)
print(password)