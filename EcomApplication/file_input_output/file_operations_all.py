import random
import json

vendors =['FLIPKART','AMAZON','SHOPCLUES','NAAPTOL','EBAY']

class Product:
    def __init__(self,pid,pname,prc,pqty,ven):
        self.product_id = pid
        self.product_name = pname
        self.product_price = prc
        self.product_qty = pqty
        self.product_vendor = str(ven)
        Product.count = Product.count+1

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

    count =1

    @classmethod
    def get_product(cls):
        return cls(pid=Product.count,
                   pname='Mobile'+str(Product.count),
                   prc=round(random.randint(5000,10000)/3,2),
                   pqty=random.randint(5,100),
                   ven=vendors[random.randint(0,len(vendors)-1)])


productList = []
for item in range(10):
    productList.append(Product.get_product())
print('----------------------------------')
print(productList)
print('----------------------------------')

file_path = 'F:\\pythonProject\\EcomApplication\\data_files\\'
# def write_data_into_textfile():
#     prodLines =[]
#     for prod in productList:
#         prodstr = str(prod.product_id)+"\t\t"+prod.product_name+"\t\t"+str(prod.product_price)+"\t\t"+str(prod.product_qty)+"\t\t"+prod.product_vendor
#         prodLines.append(prodstr)
#
#         with open(file_path+'product.text','w') as file:
#             for prod in prodLines:
#                 file.writelines(prod)
#     print('Products are written in Prodcut.txt file')
#
#     print('Raed operations of Text file...')
#
# def read_data_from_textfile():
#         with open(file_path+'product.txt','r') as file:
#             alllines = file.readlines()
#             alllines = [line.strip() for line in alllines]
#
#             prodList = []
#             for line in alllines:
#                 word =line.split('\t\t')
#                 prodList.append(Product(pid=word[0],pname=word[1],prc=word[2],pqty=word[3],ven=word[4]))
#             print(prodList)



print('Write into Product.json file....')
def write_data_into_jsonfile(productList):
    with open(file_path+'product.json','w') as file:
        file.write("[")
        for i in range(len(productList)):
            json_object = json.dumps(productList[i].__dict__, indent=2)
            file.write(json_object)
            if i != len(productList) - 1:
                file.write("," + "\n")
        file.write("]")


print('Read from Product.json file....')
def read_data_into_jsonfile():
    with open(file_path + 'product.json', 'r') as file:
        jsondict = json.load(file)
        print(jsondict)

# write_data_into_textfile()
# read_data_from_textfile()

write_data_into_jsonfile(productList)
read_data_into_jsonfile()