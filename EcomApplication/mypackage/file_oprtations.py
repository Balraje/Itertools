import random

vendors = ['FLIPKART', 'AMAZON', 'SHOPCLUES', 'NAAPTOL', 'EBAY']


class Product:
    def __init__(self, pid, pname, prc, pqty, pven):
        self.product_id = int(pid)
        self.product_name =str(pname)
        self.product_price = float(prc)
        self.product_qty = int(pqty)
        self.product_vendor = str(pven)
        Product.count = Product.count + 1

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

    count = 1

    @classmethod
    def get_product(cls):
        return cls(pid=Product.count,
                   pname='Mobile' + str(Product.count),
                   prc=round(random.randint(5000, 10000) / 3, 2),
                   pqty=random.randint(5, 100),
                   pven=vendors[random.randint(0, len(vendors) - 1)]
                   )

prodList = []
for prodcuts in range(9):
    prodList.append(Product.get_product())
print("-------------------------")
print(prodList)
print("-------------------------")

file_path = 'F:\\pythonProject\\EcomApplication\\data_files\\'
def write_data_into_text(prodList):
    prodLines = []
    for prod in prodList:
         prodstr = str(prod.product_id) + "\t\t"+ prod.product_name +"\t\t" + str(prod.product_price) +"\t\t" + str(prod. product_qty) + "\t\t"+prod.product_vendor+"\n"
         prodLines.append(prodstr)

    with open(file_path+'product.txt','w') as file:
        for prod in prodLines:
            file.writelines(prod)

    print('Products are added in Product.txt file')

    #Read from File
    print('Read from Product.txt file')
    with open(file_path+'product.txt','r') as file:
        alllines = file.readlines()
        alllines = [line.strip() for line in alllines]
        #prodList = []

        for line in alllines:
            words = line.split('\t\t')
            prodList.append(Product(pid = words[0],pname = words[1],prc= words[2],pqty = words[3],pven=words[4]))
        print(prodList)

write_data_into_text(prodList)

def write_data_into_json():
    pass

def write_data_into_csv():
    pass

def write_data_into_excel():
    pass
