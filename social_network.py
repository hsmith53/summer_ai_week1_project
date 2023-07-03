#Various import Statements can go here
from  social_network_classes import SocialNetwork, Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            name = input("What would you like your username to be? ")
            x = 0
            while x == 0:
                for person in ai_social_network.get_name_list():
                    if person == name:
                        print("This username already exists!")
                        name = input("What would you like your username to be? ")
                    else:
                        pass
                x = 1
            age = input("What is your age? ")
            while int(age) > 120 or int(age) < 0:
                print("Please enter a valid age!")
                age = input("What is your age? ")
            ai_social_network.create_account(name, age)

        elif choice == "2":
            print("")
            user = input("What is your username? ")
            user_object = None

            while True:
                for person in ai_social_network.get_person_list():
                    if person.id == user:
                        user_object = person
                        break  # Exit the loop once a match is found
        
                if user_object is None:
                    print("This username does not exist!")
                    user = input("What is your username? ")
                else:
                    break
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    innist_menu_choice = social_network_ui.edit_details_Menu()
                    while True:
                        if innist_menu_choice == "1":
                            new_name = input("What would you like your new username to be? ")
                            while new_name in ai_social_network.get_name_list():
                                print("This username already exists")
                                new_name = input("What would you like your new name to be? ")
                            user_object.change_name(new_name)
                            break
                        elif innist_menu_choice == "2":
                            new_age = input("What would you like your new age to be?")
                            user_object.change_age(new_age)
                            break
                        
                        elif innist_menu_choice == '3':
                            inner_menu_choice = social_network_ui.manageAccountMenu()
                            break
                        
                        else:
                            innist_menu_choice = social_network_ui.edit_details_Menu()
                        
                elif inner_menu_choice == '2':
                    new_friend = input("Who would you like to add as a friend? ")
                    friend_object = None

                    while friend_object is None:
                        for person in ai_social_network.get_person_list():
                            if person.id == new_friend:
                                friend_object = person

                    if friend_object is None:
                        print("This username does not exist!")
                        new_friend = input("Who would you like to add as a friend? ")

                    user_object.add_friend(friend_object)
                    print(f"You and {new_friend} are now friends!")

                    break
                

                elif inner_menu_choice == '3':
                    new_blocked = input("Who would you like to block as a friend? ")
                    blocked_object = None

                    while blocked_object is None:
                        for person in ai_social_network.get_person_list():
                            if person.id == new_blocked:
                                blocked_object = person
                                break  # Exit the loop once a match is found

                    if blocked_object is None:
                        print("This username does not exist!")
                        new_blocked = input("Who would you like to block as a friend? ")
                    
                    user_object.block_friend(blocked_object)
                    print(f"{new_blocked} is now blocked!")  

                    break

                elif inner_menu_choice == '4':
                    print("")
                    print("My friends:")
                    user_object.view_friends()
                    
                    break

                elif inner_menu_choice == '5':
                    message_user = input("Who would you like to send a message to? ")
                    message_object = None


                    while message_object is None:
                        for person in ai_social_network.get_person_list():
                            if person.id == message_user:
                                message_object = person
                                break  # Exit the loop once a match is found

                    if message_object is None:
                        print("This username does not exist!")
                        message_user = input("Who would you like to send a message to? ")

                    message = input(f"What would you like to say to {message_user}? \n")
                    user_object.send_message(message_object, message)
                    print("Your message has been sent!")

                    break 

                elif inner_menu_choice == '6':
                    print("")
                    print("My messages:")
                    user_object.view_messages()

                    break

                elif inner_menu_choice == "7":
                    break

                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()