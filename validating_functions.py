VALID_USERS = ['yusuf', 'lillie', 'ash', 'paul', 'alanna']
VALID_PASSWORDS = ['jtc4Life', 'eatPopcorn', 'yoDude', 'DrBloom', 'checkDaCalendar']

validation = False
# num_tries = 0

def validate_account():
    while validation == False:
    # while validation == False and num_tries < 3:
        current_user = input("Please enter your name: ")
        password = input("Please enter your password: ")
        if current_user.lower() in VALID_USERS and password in VALID_PASSWORDS:
            validation == True
            print("Successfully logged in.")
            print(f"Welcome {current_user.capitalize()}.")
            break
        else:
            print("Invalid username/password combination. Try again.")
        
        # if num_tries == 1:
        #     print("You have 2 attempts remaining before you are locked out of your account!")
        # elif num_tries == 2:
        #     print("You have 1 attempt remaining before you are locked out of your account!")
        # else:
        #     print("You are locked out of your account for 24 hours.")