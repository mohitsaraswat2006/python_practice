# FIND THE SUM OF FIRST N NATUTAL NUMBERS.
n = int(input("enter a any number : "))
sum = 0 
for i in range(1,n+1) :
    sum += i
    
print("total sum =",sum)
