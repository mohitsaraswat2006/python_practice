# ARITHMETIC OPERATORS.
a = 13
b = 6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#RELATIONAL OPERATORS.
a = 50
b = 20
print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)


# ASSIGNMENT OPERATORS.
num = 10
num += 10
print(num)

b = 12
b -= 11
print(b)

c = 10
c *=5
print(c)

d = 90
d /= 5
print(d)

e = 90
e /= 5
print(e)

#LOGICAL OPERATORS.
a = 10
b = 12
print(not(a > b))

val1 = True
val2 = True
print(val1 and val2)

val3 = True 
val4 = False
print(val3 or val4)

#TYPE CONVERSION. 
var1 = 12
var1 = str(12)
print(type(var1))
print(var1)


# INPUT TWO NUMBERS AND PRINT THEIR SUM.
a = int(input("enter first number : "))
b = int(input("enter second number : "))
print("sum of a and b is : ",a + b)


# INPUT SIDE OF A SQUARE AND PRINT AREA OF THE SQUARE.
side = int(input("enter a side of a square : "))
print("area os the sqaure is : ",side**2)


# INPUT TWO FLOATING POINT NUMBERS AND PRINT THEIR AVERAGE.
a = float(input("enter first number : "))
b = float(input("enter second number : "))
average = (a+b)/2
print("average of two numbers is : ",average)


# TAKE INPUT OF TWO NUMBERS, PRINT TRUE IF A IS GREATER THAN OR EQUAL TO B OTHERWISE FALSE.
a = int(input("enter first number : "))
b = int(input("enter second number : "))
 
print(a >= b) 