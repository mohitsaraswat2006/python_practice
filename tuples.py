# tuple is a immutable sequence of values inside parethesis().
tup = (8,5,9,6,7,12)
print(type(tup))
print(tup[0])
print(tup[2]) 

# if there is only one entry in the tuple.
tup2 = ("mohit",)
print(type(tup2))

print(tup[1:3])

# indexing.
print(tup.index(7))

# count of particular entry/number.
print(tup.count(1))