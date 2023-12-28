users = ['azeez', 'basit', 'shuaib', 'admin', 'mariam']

for user in users:
    if user == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for loggin in again")