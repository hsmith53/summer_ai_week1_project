# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. Block a friend")
    print("4. View all my friends")
    print("5. Send Message")
    print("6. View all my messages")
    print("7. <- Go back ")
    return input("Please Choose a number: ")

def edit_details_Menu():
    print("")
    print("1. Edit Name")
    print("2. Edit Age")
    print("3. <- Go back ")
    return input("Please Choose a number: ")