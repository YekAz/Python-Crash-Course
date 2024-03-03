cat = 'cat.txt'
dog = 'dog.txt'
# names = [cat, dog]

with open(dog) as f:
    lines = f.read()
print(lines.strip())

