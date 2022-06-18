

#This is custom exception class which is extended from Exception class
class MyError1(Exception):
    def __init__(self, arr):
        self.errormsg=arr

class MyError2(Exception):
    def __init__(self,arr):
        self.errmsg=arr


for i in range(4):#this will try to get input for 4 times from user in case of wrong input

    #This will check input is number or not
    try:
        inp1=int(input("Enter a number : "))
    except ValueError as ve:
        print("Enter only number")

    #This will check for non negative number an will use MyError1 custom exception
    try:
        if inp1<0:
                raise MyError1("Please enter non negative value..")
    except MyError1 as me1:
            print(me1)
    #This is for MyException2 custom exception
    try:
        if inp1>100:
            raise MyError2(f"Please enter value less than 100, you entered: {inp1}")
    except MyError2 as  me2:
        print(me2.errmsg)

    else:
        print(inp1)
        break

         





