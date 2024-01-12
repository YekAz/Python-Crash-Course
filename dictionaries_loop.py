user_0 = {
    'username': 'yekaz',
    'first': 'azeez',
    'last': 'yekinni'
    }

for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

###############################################

fav_numbers = {
    'azeez': 10,
    'wakeelat': 15,
    'tade': 76,
    'hafeez': 43,
    'nasir': 12,
    }

for person, number in fav_numbers.items():
    print(f"\n{person.title()} favourite number is: {number}")

########################################################
    
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in fav_languages.keys():
    print(name.title())
    if name in friends:
       language =fav_languages[name].title()
       print(f"{name.title()}, I see you love {language}!.")