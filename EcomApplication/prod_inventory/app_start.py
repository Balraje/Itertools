from prod_inventory.impl import ProductServiceImpl, Product
from vendor_info import Vendor


def take_product_input():
    '''Take input from user --> and create product object...'''
    pid = int(input('Enter Product Id : '))
    pnam = input('Enter Product Name : ')
    pqty = int(input('Enter Product Qty : '))
    prc = float(input('Enter Product Price : '))
    ven = take_vendor_input()
    cat = input('Enter Product Category : ')
    return Product(pid=pid, pnm=pnam, price=prc, pqty=pqty, pven=ven, pcat=cat)


def take_vendor_input():
    '''Take input from User and create Vendor Object'''
    vid = int(input('Enter Vendor Id : '))
    vname = input('Enter Vendor Name : ')
    vadr = input('Enter Vendor Address : ')
    return Vendor(vid, vname, vadr)


if __name__ == '__main__':
    prodService = ProductServiceImpl()
while True:
    print('''
                1 Add_product
                2 Avg_product_price
                3 Delete_product
                4 Get_all_product
                5 Max_product_price
                6 Min_product_price
                7 Search_by_category
                8 Search_by_id
                9 Search_by_vendor
                10 Total_product_price
                11 Update_product
        ''')
    choice = int(input('Enter Your Choice : '))
    if choice == 1:
        product = take_product_input()
        prodService.add_product(product)
    elif choice == 2:
        avg = prodService.avg_product_price()
        print('Average Product Price : ', avg)
    elif choice == 3:
        search_product = int(input("Enter the Product ID you want to Delete:"))
        prodService.delete_product(search_product)
    elif choice == 4:
        prodList = prodService.get_all_product()
        print('Products:', prodList)
    elif choice == 5:
        max_price=prodService.max_product_price()
        print("Maximum Price Product:", max_price)
    elif choice == 6:
        min_price = prodService.min_product_price()
        print("Minimum Price Product:", min_price)
    elif choice == 7:
        search_cate = input("Enter the Product Category you want to Search:")
        prod = prodService.search_by_category(search_cate)
        print(prod)
    elif choice == 8:
        search_pid = int(input("Enter the Product ID you want to Search:"))
        prod = prodService.search_by_id(search_pid)
        print(prod)
    elif choice == 9:
        search_ven = input("Enter the Vender name you want to Search Product:")
        prod = prodService.search_by_vendor(search_ven)
        print(prod)
    elif choice == 10:
        total = prodService.total_product_price()
        print('Total Product Price : ', total)
    elif choice == 11:
        pid = int(input("Enter the Product ID you want to Update:"))
        prodService.update_product(pid)
    else:
        print('Invalid Choice..')

    ch = input('Do you want to continue : Y/N')
    if ch.lower() in ['n', 'no']:
        break

