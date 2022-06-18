

class Vendor:

    def __init__(self,vid,vnm,ven_adr,ven_baln):
        self.vendor_id = vid
        self.vendor_name = vnm
        self.vendor_address = ven_adr
        self.vendor_balance = ven_baln

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

class Product:

    def __init__(self,pr_id,pr_name,pr_pric,category,qty,vendor):
        self.product_id = pr_id
        self.product_name = pr_name
        self.product_price = pr_pric
        self.category = category
        self.vendor = vendor
        self.quantity = qty

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)


class Customer:

    def __init__(self,cust_id,cust_nm,cust_adr,cust_balance):
        self.cust_id = cust_id
        self.cust_name = cust_nm
        self.cust_address = cust_adr
        self.cust_balance = cust_balance

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}'''




class RawItems:

    def __init__(self,name,applicablefor,price,qty):
        self.name = name
        self.applicable_for = applicablefor
        self.price = price
        self.qty = qty
       # self.numofitems = numofitems

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)


class Order:
    def __init__(self,orid,who_placed,qty,status,for_what,order_date,final_amnt):
        self.order_id = orid
        self.who_placed = who_placed
        self.qty = qty
        self.status = status
        self.for_what = for_what  #product --> individual price --
        self.order_date = order_date
        self.final_amount = final_amnt

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)