# Moving items from one list to another

unverified_users = ['Azeez', 'Wakeelat', 'Shuaib']
verified_users = [ ]

while unverified_users:
    current_user = unverified_users.pop()

    print("Verifying User:", current_user.title())
    verified_users.append(current_user)

print("\nThe following users have been confirmed:")
for verified_user in verified_users:
    print(verified_user.title())


# Filling a dictionary with user input
        
response = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    mountain = input("\nWhich mountain would you like to climb?")

    response[name] = mountain
    print(response)

    repeat = input("\nWould someone else like to tak the poll? (y/n) --- ")
    if repeat == "n":
        polling_active = False

print("---Poll Results---")
for name, mountain in response.items():
    print(name, "would like to climb", mountain)









