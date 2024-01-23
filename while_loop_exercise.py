# Movig a list of made and exhausted pastry into another list

sandwish_orders =["Beef", "pantranmy", "Chicken", "pantranmy", "Broccoli", "pantranmy", "Fish", "Tuna", "pantranmy"]
finished_sandwishes =[]

while "pantranmy" in sandwish_orders:
    sandwish_orders.remove("pantranmy")
print("Sorry, we have run out of Pantranmy\n")

while sandwish_orders:   
    made_sandwish = sandwish_orders.pop()
    finished_sandwishes.append(made_sandwish)
    print("I made your", made_sandwish)

print("\n---The following sandwishes are exhausted---")
for sandwish in finished_sandwishes:
    print(sandwish, "has been made and exhausted")




    