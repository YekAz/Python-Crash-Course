###########

unverified_users = ['Azeez', 'Wakeelat', 'Shuaib']
verified_users = [ ]

while unverified_users:
    current_user = unverified_users.pop()

    print("Verifying User:", current_user.title())
    # verified_users.append(current_user)

    print("\nThe following users have been confirmed:")
    for verified_user in verified_users:
        print(verified_user.title())

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

#     print("\nThe following users have been confirmed:")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())