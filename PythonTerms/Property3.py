class Product:
    def __init__(self, pid, pname, price):
        self.prod_id = pid
        self.prod_name = pname
        self. prod_price = price

    def __str__(self):
        return f'''Product ID: {self.prod_id}, Product Name:{self.prod_name},product Price: {self.prod_price}'''

    def get_price(self):
        if self.__dict__.__contains__('_prod_price'):
            return self._prod_price
        return ""

    def set_price(self, price):
        if type(price) == float:
            if price < 0.0:
                print("Invalid Price")
            else:
                self._prod_price = price
        else:
            print("Invalid Data")

    prod_price = property(fget=get_price, fset=set_price)

p1= Product(101,'Soap', 32.3)
print(p1)
p1.prod_price = 35.50
print(p1)