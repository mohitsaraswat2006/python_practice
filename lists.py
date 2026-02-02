# LISTS.
marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))

#INDEXING IS ALLOWED.
print(marks[0])
print(marks[2])
print(len(marks))

# LISTS CAN STORE DATA OF MAY DATATYPES.
student = ["KARAN",67,21.4,"DELHI"]
print(student)

# LISTS ARE MUTABLE.
student[0] = "mohit"
print(student)

# LIST SLICING.
list = [87,54,98,23,74,91,12]
print(list[0:2])
print(list[:4])
print(list[3:])
print(list[-3:-1])

#  APPEND(INSERING ELEMENT INTO LIST).
list2 = [2,1,3]
list2.append(4)
print(list2)

# SORT 
list2.sort()
print(list2)

# REVERSE.
list2.reverse()
print(list2)

# INSERTING AT THE GIVEN INDEX.
list2.insert(1,5)
print(list2)
list2.insert(4,78)
print(list2)

# REMOVE(TO REMOVE ANY NUMBER).
list2.remove(78)
print(list2)

# POP.
list2.pop(4)
print(list2)