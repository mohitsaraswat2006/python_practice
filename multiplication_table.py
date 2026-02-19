# n = int(input("enter a number : "))
# i = 1
# while(i<=10) :
#     print(n ,"X",i ,"=", n*i)
#     i+=1

#=====================TO SKIP MULTIPLE OF 3=======================
i = 1
while(i<=32) :
    if(i%3==0) :
        i+=1
        continue
    print(i)
    i+=1
print("end of loop.")    