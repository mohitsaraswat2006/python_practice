# class car :
#     def __init__(self,type):
#         self.type = type
        
#     @staticmethod
#     def start() :
#         print("car started.")
        
#     @staticmethod
#     def stop():
#         print("carr stopped.")
        
# class toyotacar(car) :
#     def __init__(self,name,type) :
#         self.name = name
#         super().__init__(type)
#         super().start()
        
# car1 = toyotacar("corolla","electric")
# print(car1.type)
            
#==========================================CLASS METHOD========================================

# class person :
#     name = "anonymous"
    
#     @classmethod
#     def changename(cls,name):
#         cls.name = name

#     # def changename(self,name):
#     #     # self.name = name  ## doesn't chnage  the name of person class.        
#     #     # person.name = name   
        
#     #     ##NOW WE HAVE ANOTHER WAY TO CHANGE NAME OF CLASS.
#     #     self.__class__.name = "rahul"
        
        

# p1 = person()
# p1.changename("rahul kumar")
# print(p1.name)
# print(person.name)

#========================PROPERTY DECORATOR==========================
class student :
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        
    # def calcpercentage(self) :
    #     self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"
    @property
    def percentage(self) :
        return str((self.phy + self.chem + self.maths)/3) + "%"
        
        
stu1 = student(98,97,99)
print(stu1.percentage)

stu1.phy = 86
# print(stu1.phy)
# stu1.calcpercentage()
print(stu1.percentage)


    
        
