current_users = ['soliu', 'jake', 'akanji', 'wasiu' 'albert']
new_users = ['azeez', 'soliu', 'bolaji', 'idris', 'akanji']

for new_user in new_users:
    if new_user in current_users:
        print("Please enter a new username")
    else:
        print(f"{new_user} is available")