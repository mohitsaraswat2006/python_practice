# class student :
#     subject = "python"
#     college = "bsacet"
#     year = "3rd year"

# stu1 = student() 
# print(stu1.subject,stu1.college,stu1.year)


#===========================constructor==============================
# class student :
#     def __init__(self,name,cgpa):
#         self.name = name
#         self.cgpa = cgpa

#     def get_cgpa(self) :
#         return self.cgpa

# stu1 = student("mohit",8.6)
# stu2 = student("karan",5.6) 
# stu3 = student("ravi",9.1)

# # print(stu1.name)
# # print(stu2.name)
# # print(stu3.name)

# # print(stu1.cgpa)
# # print(stu2.cgpa)
# # print(stu3.cgpa) 

# print(stu1.get_cgpa())
# print(f"{stu2.name} has {stu2.get_cgpa()} cgpa.")

#=========================class attributes & instance attributes==============================
class student :
    college_name = "bsacet" 
    PI = 3.1     #class attribute

    def __init__(self,name,cgpa) :
        self.name = name           #instance attribute
        self.cgpa = cgpa
        self.PI = 3.14

stu1 = student("rahul",8.4)
print(stu1.name)
print(stu1.college_name)
print(student.college_name)
print(stu1.PI)






