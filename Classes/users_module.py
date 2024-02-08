"""An attempt to model a Users class and store it in a module"""

class Users:
    """Attempt to model a user"""
    def __init__ (self, first_name, last_name, age, state, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.state = state
        self.sex = sex
        self.login_attempts = 0
        
    def describe_user(self):
        """Simulatig the user description from a command"""
        print(f"Your name is {self.first_name} {self.last_name}.\nYou are {self.age} years old and an indigene of {self.state} state.\nYou are {self.sex}.")

    def greet_user(self):
        """Simulating the greeting of the user from a command"""
        print(f"Welcome, {self.first_name} {self.last_name}.")

    def login_attempts_count(self):
        """Printing a statement showing the number of login attempts by a user."""
        print(f"This user has attempted to login {self.login_attempts} times.")

    def increment_login_attempts(self):
        """Attempting to create a method that increments the value of the attribute by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Attempting to create a method that resets the number of login attempts by a user."""
        self.login_attempts = 0

class Privilege:
    """An attempt create a privilege list for the admin user"""

    def __init__(self):
        """Initializing the admin's privileges"""
        self.privileges = ["can add post", "can delete post", "can ban user", "can comment", "can approve users", "can close group"]

    def show_privileges(self):
        """Printing the list of the admin's privileges"""
        print(f"Theses are the administrator's set of privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(Users):
    """Creating a child class called Admin from the parent class Users"""
    def __init__(self, first_name, last_name, age, state, sex):
        """Initializing the attributes of the parent class"""
        super().__init__(first_name, last_name, age, state, sex)
        self.privileges = Privilege()
        """Initializing attributes specific to the admin user by using the instance Privilege() created above, as an attribute."""