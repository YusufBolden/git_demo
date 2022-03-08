# Handling exceptions

# Try/except
# Multiple exceptions, else and finally

# The code will first run the try block, prompt the user for a number and print e divided by that number
try:
    x = int(input("What's the value of x?: "))
    print(4/x)
# If the user enters another datatype, it will generate a TypeError and send back this print statement
except TypeError:
    print("I need you to input a number")
# If the user enters anything other than a number, it will generate a ValueError and send back this print statement
except ValueError:
    print('You must enter a number')
# If the user enters 0, it will generate a ZeroDivisionError and send back this print statement
except ZeroDivisionError:
    print('You cannot divide by 0!')
# This print statement will be returned if some other error is generated
except:
    print('Something else went wrong!')
# This statement will be sent to user if the try block successfully runs
else:
    print("Nothing went wrong")
# This statement will always be sent to user regardless if the try block successfully runs or not
finally:
    print("We made it to the end!")
