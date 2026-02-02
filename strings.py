str1 = "this is a string"
str2 = 'mohit saraswat'
str3 = '''computer science'''

# CONCATINATION.
print(str1 + str2)

# LENTH OF ANY STRING.
print(len(str2))
print(len(str(str3)))

# INDEXING.
name = "mohit saraswat"
print(name [3])
print(name[5])

# SLICING.
hey = "i m a btech student." 
print(hey[1:7])
print(hey[0:9])
print(hey[7:len(hey)])
# 7 to full lenth of string.
print(hey[9:])
# 9 to full lenth of string.

# NEGATIVE INDEXING. => starts with -(negative maximum) number.
let = "dipawali"
print(let[-5:-1])

# STRING FUNCTIONS.
string = "i m studying python from apna college"
print(string.endswith("ege"))
print(string.endswith("stp"))

print(string.capitalize())

print(string.replace("o","a"))
print(string.replace("python","javascript"))

print(string.find("o"))
print(string.find("python"))
print(string.find("q"))

print(string.count("from"))

# TAKE INPUT OF NAME AND PRINT IT'S FIRST NAME AND PRINT IT'S LENTH ALSO.
a = input("enter your first name....")
b = input("enter your second name...")
print("your first name is : ",a)
print(len(a + b))


# FIND THE OCCURANCE OF $ SIGN IN THE STRING.
many = "this dollar ($). $ is the corrency of usa.$"
print(many.count("$"))
