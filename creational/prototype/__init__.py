import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

# using normal operator

d = c
print(id(c) == id(d))  # True - d is the same object as c
print(id(c[0]) == id(d[0]))  # True - d[0] is the same object as c[0]


# using a shallow copy

d = copy.copy(c)
print(id(c) == id(d))  # False -d is the new object
print(id(c[0]) == id(d[0]))  # True - d[0] is the same as c[0]


# using a deepcopy

d = copy.deepcopy(c)

print(id(c) == id(d))  # False -d is now a new object
print(id(c[0]) == id(d[0]))  # False -d [0] is now a new object
