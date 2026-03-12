#=============================1 to 50=============================
# for i in range(1,51):
#     print(i)

#=========================EVEN 1 TO 100===========================
# for i in range(1,101):
#     if(i % 2 == 0):
#         print(i)

#==========================ODD 1 TO 100===========================
# for i in range(1,101):
#     if(i % 2 != 0):
#         print(i)

#=====================SUM OF FIRST N NATURAL NUMBERS==============
# n = int(input("Enter any number :- "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

#=====================FACTORIAL OF NUMBER=========================
# n = int(input("Enter any number :- "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

#=====================MULTIPLICATION TABLE OF ANY NUMEBER===========
# n = int(input("Enter any number for table :- "))
# for i in range(1,11):
#     mul = n * i 
#     print(f"{n} X {i} = {mul}")

#=====================REVERSE A GIVEN NUMBER =========================
# n = int(input("Enter any number of any length :- "))
# temp = n
# rev = 0
# while n > 0 :
#     last_digit = n % 10
#     rev = rev * 10 + last_digit
#     n = int(n / 10)

# print(f"reverse of {temp} is {rev}.")

#=============================PALINDROME OR NOT===========================
# n = int(input("enter any number :- "))
# temp = n
# rev = 0
# while n > 0:
#     last_digit = n % 10
#     rev = rev * 10 + last_digit
#     n = int(n / 10)

# print(f"reverse of {temp} is {rev}.")
# if(temp == rev):
#     print(f"{temp} is a palindrome number.")
# else :
#     print(f"{temp} is not a palindrome number.")

#===========================COUNT NUMBER OF DIGITS=======================
# n = int(input("enter any number with any length :- "))
# count = 0
# while n > 0:
#     n = int(n / 10)
#     count += 1

# print(f"Given number contains {count} digits.")

#==========================SUM OF DIGITS OF ANY NUMBER===================
# n = int(input("Enter any number with any length :- "))
# sum = 0
# while n > 0:
#     last_digit = n % 10
#     sum = sum + last_digit
#     n = int(n / 10)

# print(f"Sum of digits of given number is {sum}")

#===========================FABONICCI SERIES UPTO N=====================
# n = int(input("Enter the number of terms :- "))
# n1 = 0
# n2 = 1
# sum = 0
# while n > 0:
#     print(n1)
#     sum = n1 + n2
#     n1 = n2
#     n2 = sum
#     n -= 1

#========================NUMBER IS PRIME OR NOT===========================
# n = int(input("Enter nay number :- "))
# state = True
# for i in range(2,n):
#     if(n % i == 0):
#         state = False
#         break
    
#     if state and n > 1:
#         print(n,"is a prime number.")
#     else:
#         print(n,"is not an prime number.")

#========================LARGEST DIGIT IN A NUMBER======================
# n = int(input("Enter any number :- "))
# largest = 0
# while n > 0 :
#     last_digit = n % 10
#     n = int(n / 10)
#     if( largest < last_digit):
#         largest = last_digit

# print(f"Largest digit is {largest}")

#========================RIGHT ANGLED TRAINGLE==========================
# n = int(input("Enter any number :- "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end = " ")

#     print()

#===========================10 TO 1 USING WHILE LOOP====================
n = 10
while n >= 1 :
    print(n)  
    n -= 1

    

    