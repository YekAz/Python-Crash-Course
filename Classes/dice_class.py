
import random

class Die:
    """Initializing a class Die to model a real dice with 6 sides"""
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self, sides): 
            self.sides = sides
            for i in range(1,11):
                random_number = random.randint(1,self.sides)
                print(random_number)

class six_sided_Die(Die):
    def __init__(self, sides=6):
        super().__init__(sides=6)
        self.sides = sides
        # for i in range(1,11):
        #     ten_rollings = random.randint(1,6)
        #     print(ten_rollings)

class ten_sided_Die(Die):
    def __init__(self, sides=6):
        super().__init__(sides)
        self.sides = 10
        for i in range(1,11):
            ten_rollings = random.randint(1,10)
            print(ten_rollings)

class twenty_sided_Die(Die):
    def __init__(self, sides=6):
        super().__init__(sides)
        self.sides = 20
        for i in range(1,11):
            ten_rollings = random.randint(1,20)
            print(ten_rollings)


dice = ten_sided_Die()
dice.roll_die()

