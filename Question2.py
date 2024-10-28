shopping_list = ['Bread', 'Milk', 'Sugar', 'Coffee']

def add_item(item):
    shopping_list.append(item)

def rem_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("This item is not on the list!")

while True:
    action=input("Would you like to [V]iew your list, [A]dd an item, [R]emove an item, or [Q]uit").upper()
    if action == 'V':
        print(f"Your shopping list is as follows: {shopping_list}")
    elif action == 'A':
        item_to_add = input("Enter your new item here:  ")
        add_item(item_to_add)
    elif action == 'R':
        item_to_remove = input('Enter the item you would like to remove here: ')
        rem_item(item_to_remove)
    elif action == 'Q':
        print("Goodbye!")
        break
    else:
        print("Invalid input, please try again.")




