while True:
    # Create an empty list
    my_list = []

    # Keep prompting the user for input until they enter 'done'
    while True:
        item = input("Enter an item (type 'done' to stop): ")
        if item == 'done':
            break
        my_list.append(item)

    # Print the list
    print("Your list:", my_list)

    # Ask the user which item they want to delete
    delete_item = input("Which item do you want to delete? ")

    # Check if the item is in the list and remove it
    if delete_item in my_list:
        my_list.remove(delete_item)
        print(delete_item, "has been removed from the list.")
    else:
        print(delete_item, "is not in the list.")

    # Print the updated list
    print("Your updated list:", my_list)

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
