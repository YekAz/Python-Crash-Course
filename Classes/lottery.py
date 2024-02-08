from random import choice

picks = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
pack = [ ]

print("Any tickets or letters matching these four numbers or letters wins a prize:")
for i in range(0,4):
    pick = choice(picks)
    pack.append(pick)
print(f"{pack}")





