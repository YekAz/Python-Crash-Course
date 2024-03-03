import json

username = input("Enter your username: ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)

print("We will remember when you come back")