# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = []
        self.list_of_names = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self, name, age):
        #implement function that creates account here
        self.name = name
        self.age = age
        print("Creating Account...")
        my_new_person = Person(self.name, self.age)
        self.list_of_people.append(my_new_person)
        self.list_of_names.append(my_new_person.id)
        print("Your account has been created!")
        pass
    def get_person_list(self):
        return self.list_of_people
    def get_name_list(self):
        return self.list_of_names

            



class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messages = []
    
    def __str__(self):
        return self.id
    

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(person_object) 
        pass

    def send_message(self, friend_object, message):
        #implement sending message to friend here
        if friend_object in self.friendlist:
            friend_object.messages.append('From {self.id}: "{message}"')
        else:
            print(f'{friend_object} not in friend list!')

        pass

    def block_friend(self, person_object):
        if person_object in self.friendlist:
            self.friendlist.remove(person_object)
        pass

    def view_friends(self):
        for person in self.friendlist:
            print(person)
        pass

    def view_messages(self):
        for message in self.messages:
            print(message)
        pass

    def change_name(self, new_name):
        self.id = new_name
        pass
    
    def change_age(self, new_age):
        self.age = new_age
        pass
        

    
        
