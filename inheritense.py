# ===========================SINGLR LEVEL INHERITENCE=====================
# class car :
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started.")

#     @staticmethod
#     def stop() :
#         print("car staopped.")

# class toyotacar(car) :
#     def __init__(self,name):
#         self.name = name

# car1 = toyotacar("fortuner")
# car2 = toyotacar("corolla")
# # print(car1.name)
# print(car1.start())
# print(car1.color)

# ===============================MULTI LEVEL INHERITENSE=====================

# class car :
#     @staticmethod
#     def start():
#         print("car started.")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotacar(car) :
#     def __init__(self,brand):
#         self.name = brand


# class fortuner(toyotacar) :
#     def __init__(self,type):
#         self.type = type
    
# car1 = fortuner("diesel")
# car1.start()

# ========================================MULTIPLE INHERITANCE================

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

C1 = C()
print(C1.varC)
print(C1.varA)
print(C1.varB)
        