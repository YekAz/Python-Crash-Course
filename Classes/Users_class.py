# Creating a class called Users

class Users:
    """Attempt to model a user"""
    def __init__ (self, first_name, last_name, age, state, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.state = state
        self.sex = sex
        
    def describe_user(self):
        """Simulatig the user description from a command"""
        print(f"Your name is {self.first_name} {self.last_name}.\nYou are {self.age} years old and an indigene of {self.state} state.\nYou are {self.sex}.")

    def greet_user(self):
        """Simulating the greeting of the user from a command"""
        print(f"Welcome, {self.first_name} {self.last_name}.")


# Creating several instaces of the class User and calling both methods for each user

user1 = Users("Azeez", "Yekinni", "30", "Ogun", "Male")
user1.describe_user()
print()
user1.greet_user()
print()

user2 = Users("Wakeelat", "Adeyemo-Yekinni", "25", "Osun", "Female")
user2.describe_user()
print()
user2.greet_user()
print()

user3 = Users("Ajibola", "Hakeem", "23", "Ilorin", "Male")
user3.describe_user()
print()
user3.greet_user() 