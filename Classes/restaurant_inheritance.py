"""Creating a child class called IceCreamStand from the Restaurant class that inherits the attributes of the parent class and also has its own specific attribute and method."""

class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine):
        """Initializing the restaurant name and cuisine type attributes."""
        self.name = name
        self.cuisine = cuisine
        """Initialized this attribute with default value to be able to change the value of the attribute number_served directly."""
        self.number_served = 0

    def describe_restaurant(self):
        """Simulating printing of the name and cuisine type of the restaurant from a command."""
        print(f"The name of the restaurant is {self.name} and they have the {self.cuisine} cuisine.")

    def open_restaurant(self):
        """Simulating the opening of the restaurant from a command"""
        print(self.name, "is opened !!!...")
    
    def number_served_count(self):
        """Printing a statement showing the number of customers served by the restaurant"""
        print(f"The restaurant has served {self.number_served} customers.")

    def set_number_served(self, number):
        """Attempting to create a method that allows you to set the number of customers served."""
        self.number_served = number

    def increment_number_served(self,number):
        """Attempting to create a method that modifies the value of the attribute, number_served, by incrementing it."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """Creating a child class IceCreamStand from the parent class Restaurant"""
    def __init__(self,name,cuisine):
        """Initializing attributes of the parent class"""
        super().__init__(name,cuisine)
        self.flavors = ["vanilla","strawberry", "chocolate", "ginger", "buttermint"]
        """Initializing attributes specific to the child class, IceCreamStand."""
    
    def flavor(self):
        """Creating a method for the child class that list out the flavors of ice-cream available."""
        print(f"This is the list of ice-cream flavours available")
        for flav in self.flavors:
            print(f"- {flav}")

IceCreamStand = IceCreamStand("BigBite", "African")
IceCreamStand.flavor()