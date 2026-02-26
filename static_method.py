# class student :
#     @staticmethod
#     def hello() :
#         print("hello")

# student.hello()

#=====================PRACTICE PROBLEM===========================
class Account :
    def __init__(self,bal,acc) :
     self.balance = bal
     self.account_no = acc  

     #debit amount.
    def debit(self,amount) :
       self.balance -=amount
       print("Rs.", amount,"was debited.")
       print("total balance",self.get_bal())

    #credit amount.
    def credit (self,amount) :
       self.balance += amount
       print("Rs.",amount,"was credited.")
       print("total balance",self.get_bal())
    
    # final balance
    def get_bal(self) :
       return self.balance


acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no) 
acc1.debit(1000)
acc1.credit(5000)