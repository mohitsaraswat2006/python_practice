# class student :
#     college_name = "BSACET"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student to database....")
    
# s1 = student("gopal" ,65) 
# print(s1.name,s1.marks)
# print(s1.college_name) # we can show any attribute with object name.  

# s2 = student("mohit",87)
# print(s2.name, s2.marks)
# print(student.college_name) #we can show attribute with class name also.

# ================another example=============

# class car :
#     color = "blue"
#     brand = "marcedes"

# car1 = car()
# print(car1.color)
# print(car1.brand)  


#====================methods========================
# class student :
#     college_name = "BSACET"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def welcome(self) :
#         print("wecome student ,", self.name) 

#     def marks(self) :
#         print(self.marks)       
    
# s1 = student("gopal" ,65) 
# s1.welcome()
# print(s1.marks)

#===========================PRACTICE QUESTION OF OOPs CONCEPT=====================
class student :
    def __init__(self,name,marks) :
        self.name = name
        self.marks = marks

    def  get_avg(self) :
        sum = 0
        for val in self.marks :
            sum += val
        print("hi",self.name,"your avg scrore is :",sum/3)    

s1 = student("tony stark ",[98,99,97]) 
s1.get_avg()
s1.name = "mohit saraswat"
s1.get_avg()
