def fullName(firstName, lastName):
    """A function that takes first name and last name and returns a well formatted fullname"""

    # firstName = input("Enter your first name: ")
    # lastName = input("Enter your last name: ")
    fullname = f"\nYour fullname is {firstName.title()} {lastName.title()}."
    return fullname

name = fullName('azeez', 'yekinni')
print(name)
