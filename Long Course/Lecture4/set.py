setName = {1, 2, 3, 4, "Dhaka"}
print(setName)
print(type(setName))
# We can not store Dictionary, list values is the set as we cannot change/update a set .
# Set is mutuable means we can add/remove values in the set but set elements are not mutuable that is
# we can not chnage the already added values of a set .
setName.add("New Item Added")
print(setName)
"""Like this we added new value in the set but we cannot chnagew this value further ,
# we need to delete this and then addd a new one"""
