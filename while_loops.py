# Countries you have visited

prompt = "Which country have you visited: "
prompt += "\nEnter 'quit' to exit. "

while True:
    country = input(prompt)

    if country == 'quit':
        break
    else:
        print(country)

# Odd numbers between 1 and 10
        
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)


# Pizza Toppings
    
pizza_toppings = " "
while True:
    pizza_toppings = input("Which topping would you like ? ")
    if pizza_toppings == "quit":
        break
    print("OK, I would add", pizza_toppings)
    print()

# Movie Ticket Price

age = 0
active = True
while active:
    age = int(input("How old are you? "))
    if age < 3:
        print("Your ticket price is free")
    if age >= 3 and age <= 12:
        print("Your ticket price is $10")
    if age > 12:
        print("Your ticket price is $15")

    payment = input("Would you like to proceed to make payments ? y/n --- ")
    if payment.lower() == "y":
        print("Proceed to the next counter. Enjoy your movie.")
    if payment.lower() == "n":
        print("Alright, see you some other time.")
    active = False


    
    

