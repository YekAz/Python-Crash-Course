# with open('learning_python.txt') as file_object:
#     contents = file_object.read()
# print(contents.strip() * 3)

filename = 'guest_book.txt'

while True:
    import datetime
    date = datetime
    guest_name = input("What is your name: ")

    with open(filename, 'a') as file_object:
        file_object.write(f"Hello {guest_name}\n")
        file_object.write(f"Your time of visit is today\n\n")

    quit = input("Are there anymore guests? y/n > ")
    if quit.lower() == "y":
        continue
    else:
        break