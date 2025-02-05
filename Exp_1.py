# Strings in Python
# Assigning string to a variable
a = 'This is a string'
print (a)
b = "This is a string"
print (b)
c= '''This is a string'''
print (c)


# Lists in Python
# Declaring a list
L = [1, "a" , "string" , 1+2]
print (L)
#Adding an element in the list
L.append(6) 
print (L)
#Deleting last element from a list
L.pop()
print (L)
#Displaying Second element of the list
print (L[1])


# Tuples in Python
tup = (1, "a", "string", 1+2)
print(tup)
print(tup[1])


# Dictionaries in Python
# A Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.

d = {1: 'Lorem', 2: 'Ipsum', 3: 'Dolerum'}
print(d)
{1: 'Lorem', 2: 'Ipsum', 3: 'Dolerum'}
# Create a Dictionary
# create dictionary using { }
d1 = {1: 'Game', 2: 'of', 3: 'Thrones'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "House", b = "of", c = "Cards")
print(d2)


# Accessing Dictionary Items
d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))


# Adding and Updating Dictionary Items

d1 = {1: 'Ruturaj', 2: 'Yogesh', 3: 'Patil'}
print(d1)

d2 = dict(a = "Ruturaj", b = "Pranavakumar", c = "Lokesh")
print(d2)
d1.pop(1)
print(d1)