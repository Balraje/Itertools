from prod_inventory.services import ProductServices, Product

class ProductServiceImpl(ProductServices):

    productList = []
    venProdList = []

    def add_product(self, prod: Product):  # instance
        if type(prod) == Product:  # prod --> XXX : str --> validation --fail
            if prod.prodId > 0:
                if prod.prodPrice > 0.0:

                    result = self.search_by_id(prod.prodId)  # Product or None
                    if result:
                        print('Duplicate Product')
                    else:
                        ProductServiceImpl.productList.append(prod)  # product will be added inside list-->
                        print('Product Added Successfully...')
                else:
                    print('Invalid Product ProductPrice')
            else:
                print('Invalid Product Id')
        else:
            print('Invalid Product Type....Product Cannot be added..')

    def avg_product_price(self):
        try:
            totalProductPrice = self.total_product_price()
            avgPrice = totalProductPrice / len(ProductServiceImpl.productList)
            return avgPrice
        except ZeroDivisionError:
            print("No any Product Exist..")


    def delete_product(self, pid: int):
        if type(pid) == int:
            for i in range(len(ProductServiceImpl.productList)):
                if ProductServiceImpl.productList[i].prodId == pid:
                    del ProductServiceImpl.productList[i]
                    print("Product Deleted Successfully....")
                    break
            else:
                print(pid, "Product Not Exist")

    def get_all_product(self):
        return ProductServiceImpl.productList

    def max_product_price(self):
        maximum = ProductServiceImpl.productList[0].prodPrice
        for i in range(len(ProductServiceImpl.productList) - 1):
            if ProductServiceImpl.productList[i + 1].prodPrice > maximum:
                maximum = ProductServiceImpl.productList[i + 1].prodPrice
        return maximum

    def min_product_price(self):
        minimum = ProductServiceImpl.productList[0].prodPrice
        for i in range(len(ProductServiceImpl.productList) - 1):
            if ProductServiceImpl.productList[i + 1].prodPrice < minimum:
                minimum = ProductServiceImpl.productList[i + 1].prodPrice
        return minimum

    def search_by_category(self, cate: str):
        if type(cate) == str:
            for prod in ProductServiceImpl.productList:
                if prod.prodCategory == cate:
                    return prod
        else:
            print('Invalid Product Category....')

    def search_by_id(self, pid: int):  # Product[Present] ya fir --> None[Absent]
        if type(pid) == int:
            for prod in ProductServiceImpl.productList:
                if prod.prodId == pid:
                    return prod
        else:
            print('Invalid Product ID....')

    def search_by_vendor(self, ven: str):
        if type(ven) == str:
            for prod in ProductServiceImpl.productList:
                if prod.prodVendor.vendorName == ven:
                    ProductServiceImpl.venProdList.append(prod)
            return ProductServiceImpl.venProdList
        else:
            print("Invalid vender Name....")

    def total_product_price(self):
        totalPrice = 0.0
        for prod in ProductServiceImpl.productList:
            totalPrice = totalPrice + (prod.prodPrice * prod.prodQty)
        return totalPrice

    def update_product(self, pid: int):
        if type(pid) == int:
            for i in range(len(ProductServiceImpl.productList)):
                if ProductServiceImpl.productList[i].prodId == pid:
                    price = float(input("Enter the Price to Update:"))
                    ProductServiceImpl.productList[i].prodPrice = price
                    print("Product Price Updated Successfully...")
                    break
            else:
                print(pid, "Product ID Does Not Exist")
        else:
            print(" Invalid Product ID")