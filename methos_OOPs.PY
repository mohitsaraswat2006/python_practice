# class laptop :
#     storage_type = "ssd"

#     def __init__(self,RAM,storage):
#         self.RAM = RAM
#         self.storage = storage

#     def get_info(self) :
#         print(f"laptop has {self.RAM} RAM & and {self.storage} storage with {self.storage_type}")

# l1 = laptop("12gb" , "512gb")
# l1 = laptop("8gb" , "256gb")

# l1.get_info()


#==================================DELETE KEYWORD ===============================
# class student :
#     def __init__(self,name):
#         self.name = name 

# s1 = student("mohit")
# print(s1)
# del s1
# print (s1)

# print(s1.name)
# del s1.name
# print(s1.name)

#====================================PRIVATE KEYWORD=============================
class person :
    __name = "anonymous"

    def __hello():
        print("hello person!")

p1 = person()
print(p1.__name)
        
print(p1.__hello)
