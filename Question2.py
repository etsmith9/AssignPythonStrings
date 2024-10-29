#task1

#Task 1: Input Length Validator Write a script that asks for and 
# checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

def user_data(first_name, last_name):
    for first in first_name:
        if len(first_name) < 2:
            print("Invalid input, must include at least two characters in first name.")
            return False
        if len(last_name) < 2:
            print("Invalid input, must include at least two characters in last name.")
            return False
        return True

while True:
    user_input = input("Please enter your first and last name to see if they are valid: (ie. John Smith)  ")
    names = user_input.split()

    if len(names) != 2:
        print("Please enter both first and last name.")
        continue
    
    first_name, last_name = names
    if user_data(first_name, last_name):
        print(f"Valid names entered! Welcome: {user_input}! ")

    continue_input = input("Would you like to check another user name? (yes/no) ").lower()
    if continue_input != 'yes':
        break