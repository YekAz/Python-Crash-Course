# Defining a function
def make_shirt(text,size="large"):
    print("The size of the shirt is", size, "and the text on the shirt is", text)

#Calling the function using positional arguments
make_shirt(text="I love Python")
#Calling the function using keyword argument
make_shirt(text="I love Python")

# Return a simple value and creating optional parameters by assigning them to empty strings
def full_name(firstname, lastname, middlename= ""):
    fullname = f"{firstname} {lastname} {middlename}"
    return fullname.title()

qari = full_name("sudais", "minshawi", "abdullah")
print(qari)

# Returning a dictionary
def build_person(first_name,last_name,age=None):
    person = {'first': first_name, 'last':last_name, 'age': age}
    return person

sohaabah = build_person("abdurrahmon", "bn auf", 65)
print(sohaabah)

##################
def city_names(city, country):
    city_country = f"{city}, {country}"
    return city_country.title()

nijja = city_names("lagos", "nigeria")
print(nijja)
spain = city_names("madrid", "espanyol")
print(spain)
italo = city_names("leece", "italy")
print(italo)

# Qur'an Recitation
def quran_recitation(qari, surah, ayah=None):
    quran = {'Qari': qari, 'Surah': surah, 'Ayah': ayah}
    return quran

# main = quran_recitation('Sudais', 'Mulk')
# print(main)
while True:
    print("Enter the name of reciter and surah.")
    print("(Enter 'q' to quit at anytime)\n")
    reciter = input("Reciter: ")
    if reciter == "q":
        break
    read = input("Surah: ")
    if read == "q":
        break
    main = quran_recitation(reciter,read)
    print(main)




