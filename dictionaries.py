alien_0 = {'color':'green', 'points':5}

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

new_point = alien_0['points']
print(f"You have earned {new_point} points.")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Starting with an empty list

alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)

# Modifying values in a dictionary

alien_2 = {'color': 'blue'}
print(f"The alien is {alien_2['color']}.")

alien_2['color'] = 'red'
print(f"The alien is now {alien_2['color']}.")
