# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.strip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())


filename = 'write_into.txt'
love = "I love programming"
with open(filename, 'w') as file_object:
    file_object.write(love)
    


