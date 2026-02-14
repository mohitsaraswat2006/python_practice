def factorial(n) :
    i = 1
    fact = 1
    while(i <= n):
        fact *= i
        i +=1
    return fact

print(factorial(4))        

# using for loop.
def factor(m) : 
    fact = 1
    for i in range(1,m+1) :
        fact *= i
    return fact

print(factor(5))
