# from validating_functions import validate_account

validation = False
num_tries = 0
user = "yusuf"
valid_password = "jtc_Spr2022"

while validation == False and num_tries < 3:
    current_user = input("Please enter your name: ")
    password = input("Please enter your password: ")
    if current_user.lower() in user and password in valid_password:
        validation == True
        print("Successfully logged in.")
        print(f"Welcome {user.capitalize()}.")
        break
    else:
        print("Invalid username/password combination. Try again.")
        num_tries += 1

    if num_tries == 1:
        print("You have 2 attempts remaining before you are locked out of your account!")
    elif num_tries == 2:
        print("You have 1 attempt remaining before you are locked out of your account!")
    else:
        print("You are locked out of your account for 24 hours.")

# Multiple users using a list and same password
# validation = False
# num_tries = 0

# VALID_USERS = ['yusuf', 'lillie', 'ash', 'paul', 'alanna']
# valid_password = "jtc_Spr2022"

# while validation == False and num_tries < 3:
#     current_user = input("Please enter your name: ")
#     password = input("Please enter your password: ")
#     if current_user.lower() in VALID_USERS and password in valid_password:
#         validation == True
#         print("Successfully logged in.")
#         print(f"Welcome {current_user.capitalize()}.")
#         break
#     else:
#         print("Invalid username/password combination. Try again.")
#         num_tries += 1

#     if num_tries == 1:
#         print("You have 2 attempts remaining before you are locked out of your account!")
#     elif num_tries == 2:
#         print("You have 1 attempt remaining before you are locked out of your account!")
#     else:
#         print("You are locked out of your account for 24 hours.")


# validate_account()