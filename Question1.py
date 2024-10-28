#task1


def addition(a, b):
    return a + b

result = addition(10, 3)
print(result)

def subtraction(a, b):
    return a - b

result = subtraction(10, 3)
print(result)

def multiplication(a, b):
    return a * b

result = multiplication(10, 3)
print(result)

def division(a, b):
    if b == 0:
        return "You cannot divide by zero!"
    return a / b

result = division(10, 3)
print(result)

 #task2

def calculation():
    while True:
        print("What type of calculation would you like to do? [A]ddition, [S]ubtraction, [M]ultiplication, or [D]ivision?")
        action = input("Enter choice: [A] [S] [M] [D]").upper()

        if action == 'A':
            number_x = int(input("Enter a number, please : "))
            number_y = int(input("Enter another number, please: "))
            totaladd = (number_x + number_y)
            print(f"Your total is {totaladd}")
        elif action == 'S':
            number_x = int(input("Enter a number, please : "))
            number_y = int(input("Enter another number, please: "))
            totalsub = number_x - number_y
            print(f"Your total is {totalsub}")
        elif action == 'M':
            number_x = int(input("Enter a number, please : "))
            number_y = int(input("Enter another number, please: "))
            totalmult = number_x * number_y
            print(f"Your total is {totalmult}")
        elif action == 'D':
            number_x = int(input("Enter a number, please : "))
            number_y = int(input("Enter another number, please: "))
            if number_y != 0:
                totaldiv = number_x / number_y
                print(f"Your total is {totaldiv}")
            else:
                print("You cannot divide by zero, please try again.")

        else:
            print("Invalid input, goodbye.")
            break

calculation()