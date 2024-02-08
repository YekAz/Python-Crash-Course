# Creating a class called Restaurant

class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine):
        """Initializing the restaurant name and cuisine type attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Simulating printing of the name and cuisine type of the restaurant from a command."""
        print(f"The name of the restaurant is {self.name} and they have the {self.cuisine} cuisine")

    def open_restaurant(self):
        """Simulating the Opening of the restaurant from a command"""
        print(self.name, "is opened !!!...")


# Making different instances or objects of the class Restaurant and calling the two methods describe_restaurant() and open_restaurant for each instance 
        
restaurant = Restaurant("BIg Bite", "BUrger")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("EatWell", "African")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("BelleFull", "American")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("Indices", "Chinese")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()


