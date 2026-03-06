class product():
    count = 0

    def __init__(self, name ,price):
        self.name = name
        self.price = price
        product.count += 1

    def get_info(self) :
        print(f"price of {self.name} is Rs.{self.price} .")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount/100)}")


p1 = product("phone" , 10000)
p2 = product("laptop" , 50000)
p3 = product("pen" , 10)

p1.get_info()
product.get_count()

p1.calc_discount(p1.price,12)

