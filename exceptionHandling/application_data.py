import sys

from custom_types import *

vendor_list  = []

def user_input_for_vendor():
    for i in range(3):
        try:
            num = int(input('Enter Number of vendors : '))
        except ValueError as e:
            print(f"Please Enter Valid Input.. Only {2-i} Attempt left.." )
        else:
            if num>0:
                for item in range(num):
                    for i in range (3):
                        try:
                            vid = int(input('Enter Vendor Id : '))
                        except ValueError as er:
                            print(f"Please enter only numeric value for Vendor ID..\nOnly {2-i} Attempt left..")
                        else:    
                            vnm = input('Enter Vendor Name : ')
                            ven_adr = input('Enter Vendor Address : ')
                            for i in range(3):
                                try:
                                    ven_baln = float(input('Enter Vendor Balance : '))
                                except ValueError as err:
                                    print(f"Please Enter Valid Balance (Numeric value expected)\nOnly {2-i} Attempt left..")
                                else:
                                    vendor = Vendor(vid,vnm,ven_adr,ven_baln)
                                    vendor_list.append(vendor)
                                    print('--'*50)
                                    break
                            break
                
            break
    

raw_material_list = []
def user_input_for_rawitems():
    for i in range (3):
        try:
            num = int(input('Enter Number of Raw Items : '))
        except ValueError as err:
            print("Please entre valid Number for RAW item ...")
        else:
            if num > 0 and num<=4:
                for item in range(num):
                    nm = input('Enter Raw Item Name : ')
                    applicable_for = input('Enter Raw Item Applicable for : ')
                    for i in range (3):
                        try:
                            price = float(input('Enter Price : '))
                            qty = int(input('Enter Quantity : '))
                        except ValueError as ve:
                            print("Please enter valid Price or Quantity...")
                        else:    
                            rawitems = RawItems(nm,applicable_for,price,qty)
                            raw_material_list.append(rawitems)
                            print('--' * 50)
                            break
            break


c1 = Customer(9911,'Mr AAA',"Pune",3894.45)
final = 1.40



class Invalid_material(Exception): #USER DEFINED EXCEPTION
    def __init__(self,error):
        self.error_msg=error

count = 1
num_of_products = {"A" : 2,"B":1,"C":3,"D":1.5}
product_list = []
def manf_products():
    global count
    if not raw_material_list:
        print('Products cannot be manf - NO Raw Material Available..')
        sys.exit(0)
    print('A --> Fiber , B--> Chemical, C--> Gases, D---> Plastics')
    
    for i in range (3):
        try:
            choice = input('Enter Your Choice : [A,B,C,D]')
            
            if choice.lower() not in ('a','b','c','d'):
                raise Invalid_material("Please enter correct choice..")
        except Invalid_material as im:
            print('Please enter correct choice..')

        else:
            if choice.upper() == 'A':
                pr_name = "FiberProduct"
                for rawitem in raw_material_list:
                    if rawitem.name.lower() == 'fiber':
                        rqty = rawitem.qty
                        num = num_of_products.get('A')
                        rprice = (rawitem.price * num) * final
                        break
                remaining_products = rqty%num       #remaining_products = 1
                numofproducts = (rqty-remaining_products)/num  #22
                rawitem.qty = remaining_products  #1
                qty = numofproducts
                pr_pric  = rprice
                category = "A"
                vendor = None
                pr = Product(count,pr_name,pr_pric,category,qty,vendor)
                product_list.append(pr)
                break
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
                product_list.append(pr)
                break
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
                product_list.append(pr)
                break
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
                product_list.append(pr)
                break
            count = count + 1
            
      
          


r1 = RawItems(name="fiber",applicablefor="A",price=100.00,qty=105)
r2 = RawItems(name="chemical",applicablefor="B",price=287.34,qty=145)
r3 = RawItems(name="gases",applicablefor="C",price=58.34,qty=435)
r4 = RawItems(name="plastic",applicablefor="D",price=28.34,qty=465)

raw_material_list.append(r1)
raw_material_list.append(r2)
raw_material_list.append(r3)
raw_material_list.append(r4)
if __name__ == '__main__':
    #user_input_for_vendor()
    #user_input_for_rawitems()
    #raw_material_list.clear() #empty
    #print(raw_material_list)
    manf_products()
    print(product_list)
    print(raw_material_list)