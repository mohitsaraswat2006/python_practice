#  SETS IN PYTHON.
collection = {1,2,3,4,5,"mohit",2}
# ignores repeated values.
print(collection)
print(type(collection))

# DUPLICATE ITEMS WILL ALSO IGNORED IN COUNTING ALSO. 
print(len(collection))

# TO PRINT EMPTY SET.
set1 = set() #empty set syntax.
print(type(set1))

# METHODS IN SET.
collection.add(12)
collection.add(22)
collection.add(23)
print(collection)
collection.remove(1)
collection.add("mohit")
collection.add((7,8,9,5))
# collection.add([7,8,9,5])
print(collection)

# to empties the set.
collection.clear()
print(len(collection))

# remove any random values.
collection2 = {1,2,"mohit","saraswat","apna","college","python"}
print(collection2.pop())
print(collection2)

# combine both set values and return new.
set2 = {1,2,3}
set3 = {3,4,5}
print(set2.union(set3))
 

 # to find common values.
print(set2.intersection(set3))