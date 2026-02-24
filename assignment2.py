#=========================TAX RATE BASED ON THE SALERY=============================
# s = int(input("enter your salery of one month : "))
# if(s < 30000):
#     print("your tax rate is 5%")
# elif(s <= 70000 and s >=30000) :
#     print("your tax rate is 15%")
# else:
#     print("your tax rate is 25%")

#=============================PRINT EVEN NUMBER USING FUNCTION=====================
# def even_num(a,b) :
#     if a < b:
#         for i in range(a+1,b) :
#             if(i%2==0) :
#                 print(i)
#     else :
#         for i in range(b+1,a) :
#          if(i%2==0) :       
#             for i in range(b+1,a) :
#                 print(i)
#     return i                    
# a = int(input("enter the starting number : "))
# b = int(input("enter the ending number : "))
# print(even_num(a,b))


#================================REVERSE ANY NUMBER =================================\
# num = int(input("enter any number : "))
# reverse = 0
# while num > 0 :
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("reversed number is : ",reverse)


#==============================PALINDROME USING LOOPS=================================
# num = int(input("enter any number : "))
# original = num
# reverse = 0
# while num > 0 :
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("reversed number is : ",reverse)

# if(reverse == original) :
#     print("number is palindrome. ")

# else :
#     print("number is not paalindrome.")

#===============================count no. of digits in any number=====================
# num = input("enter your number : ")
# count = 0
# for digit in num :
#     count += 1
# print(count)