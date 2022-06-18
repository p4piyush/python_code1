

class Product:

    def __init__(self,pid,pnm,pqty,prc,pven,pcat):
        self.product_id = pid
        self.product_name = pnm
        self.product_qty = pqty
        self.product_price = prc
        self.product_vendor = pven
        self.product_category = pcat

    def __str__(self): return f'''{self.__dict__}'''
    def __repr__(self): return str(self)


class InvalidProductName(Exception):

    def __init__(self,error):
        self.error_message = error


products = []

def product_input():
    while True:
        name = input('Enter Product Name : ')
        if name.isnumeric() or len(name)<2:
            raise InvalidProductName("Product name cannot be empty/numeric..!")
        try:
            pid = int(input('Enter Product Id : '))
        except ValueError as v:
            print('Invalid Product Id  ')
        else:
            try:
                pqty = int(input('Enter Product Qty : '))
            except:
                print('Invalid Product Quantity  ')
            else:
                try:
                    price = float(input('Enter Product Price : '))
                except ValueError as v:
                    print('Invalid Product Price ')
                else:
                    vendor = input('Enter Vendor Name : ')
                    category = input('Enter Product Category : ')
                    product = Product(pid,name,pqty,price,vendor,category)
                    products.append(product)

        print('--' * 40)
        choice = input('Do you want enter more values : Y | N : ')
        if choice.lower() in ['n', 'no']:
            break

try:
    product_input()
except InvalidProductName as p:
    print(p.error_message)

print(products)
