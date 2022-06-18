import sys

from custom_types import *

vendor_list  = []


def user_input_for_vendor():
    num = int(input('Enter Number of vendors : '))
    if num>0:
        for item in range(num):
            vid = int(input('Enter Vendor Id : '))
            vnm = input('Enter Vendor Name : ')
            ven_adr = input('Enter Vendor Address : ')
            ven_baln = float(input('Enter Vendor Balance : '))
            vendor = Vendor(vid,vnm,ven_adr,ven_baln)
            vendor_list.append(vendor)
            print('--'*50)


raw_material_list = []
def user_input_for_rawitems():
    num = int(input('Enter Number of Raw Items : '))
    if num > 0 and num<=4:
        for item in range(num):
            nm = input('Enter Raw Item Name : ')
            applicable_for = input('Enter Raw Item Applicable for : ')
            price = float(input('Enter Price : '))
            qty = int(input('Enter Quantity : '))
            rawitems = RawItems(nm,applicable_for,price,qty)
            raw_material_list.append(rawitems)
            print('--' * 50)

c1 = Customer(9911,'Mr AAA',"Pune",3894.45)
gstamnt = 1.10
profit = 1.30
final = 1.40

count = 1
num_of_products = {"A" : 2,"B":1,"C":3,"D":1.5}
product_list = []
def manf_products():
    global count
    if not raw_material_list:
        print('Products cannot be manf - NO Raw Material Available..')
        sys.exit(0)
    print('A --> Fiber , B--> Chemical, C--> Gases, D---> Plastics')
    choice = input('Enter Your Choice : [A,B,C,D]')
    if choice.upper() == 'A':
        pr_name = "FiberProduct"
        for rawitem in raw_material_list:
            if rawitem.name.lower() == 'fiber': #name is name given to raw item in LIST
               rqty = rawitem.qty #qty is quantity as input given by user which is stored in LIST
               num = num_of_products.get('A')
               rprice = (rawitem.price * num) * final #this will give finished product price
               break

        remaining_products = rqty%num       #remaining_products = 1
        numofproducts = (rqty-remaining_products)/num  #22
        rawitem.qty = remaining_products  #1
        qty = numofproducts
        pr_pric  = rprice
        category = "A"
        vendor = None
        pr = Product(count,pr_name,pr_pric,category,qty,vendor)
    elif choice.upper() == 'B':  #b B -- Upper() -- B == B
        pr_name = "ChemicalProduct"
        for rawitem in raw_material_list:
            if rawitem.name.lower() == 'chemical':
                rqty = rawitem.qty
                num = num_of_products.get('B')
                rprice = (rawitem.price * num) * final
                break

        remaining_products = rqty % num  # remaining_products = 1
        numofproducts = (rqty - remaining_products) / num  # 22
        rawitem.qty = remaining_products  # 1
        qty = numofproducts
        pr_pric = rprice
        category = "B"
        vendor = None
        pr = Product(count, pr_name, pr_pric, category, qty, vendor)
    elif choice.upper() == 'C':
        pr_name = "GasesProduct"
        for rawitem in raw_material_list:
            if rawitem.name.lower() == 'gases':
                rqty = rawitem.qty
                num = num_of_products.get('C')
                rprice = (rawitem.price * num) * final
                break

        remaining_products = rqty % num  # remaining_products = 1
        numofproducts = (rqty - remaining_products) / num  # 22
        rawitem.qty = remaining_products  # 1
        qty = numofproducts
        pr_pric = rprice
        category = "C"
        vendor = None
        pr = Product(count, pr_name, pr_pric, category, qty, vendor)
    elif choice.upper() == 'D':
        pr_name = "PlasticProduct"
        for rawitem in raw_material_list:
            if rawitem.name.lower() == 'plastic':
                rqty = rawitem.qty
                num = num_of_products.get('D')
                rprice = (rawitem.price * num) * final
                break

        remaining_products = rqty % num  # remaining_products = 1
        numofproducts = (rqty - remaining_products) / num  # 22
        rawitem.qty = remaining_products  # 1
        qty = numofproducts
        pr_pric = rprice
        category = "D"
        vendor = None
        pr = Product(count, pr_name, pr_pric, category, qty, vendor)

    count = count + 1
    product_list.append(pr)


r1 = RawItems(name="fiber",applicablefor="A",price=100.00,qty=105)
r2 = RawItems(name="chemical",applicablefor="B",price=287.34,qty=145)
r3 = RawItems(name="gases",applicablefor="C",price=58.34,qty=435)
r4 = RawItems(name="plastic",applicablefor="D",price=28.34,qty=465)

raw_material_list.append(r1)
raw_material_list.append(r2)
raw_material_list.append(r3)
raw_material_list.append(r4)
if __name__ == '__main__':
    user_input_for_vendor()
    #user_input_for_rawitems()
    #raw_material_list.clear() #empty #This will clear the list of RAW material
    print(vendor_list)
    print(raw_material_list)
    manf_products()
    print(product_list)
    print(raw_material_list)