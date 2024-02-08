# Creating a class called Users and then including a method that counts the number of login attempts by a user.

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


# Creating an instace of the class User and calling the increment_login_attempts() method several times and then reseting the login attempts to zero by calling the reset_login_attempts() method.

user1 = Users("Azeez", "Yekinni", "30", "Ogun", "Male")
user1.describe_user()
print()
user1.greet_user()
user1.login_attempts_count()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.login_attempts_count()
user1.reset_login_attempts()
user1.login_attempts_count()
