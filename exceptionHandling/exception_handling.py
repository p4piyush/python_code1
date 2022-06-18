
class InvalidAge(Exception):

    def __init__(self,error):
        self.error_message = error


class InvalidEmail(Exception):

    def __init__(self, error):
        self.error_message = error



userlist = []
def user_input():
    while True:
        values = {}
        name = input('Enter Your Name :')
        email = input('Enter Your Email Address : ')

        for item in range(3):
            try:
                age = int(input('Enter Your Age : '))  #invalid input --> code-- stop hereitself..
                if age<10 or age>60:
                    raise InvalidAge("Age Should be in between >10 and <60")        # InvalidAge -->
            except ValueError as e:  # BaseException
                print('Invalid Age...')
            else:
                values["Name"]  = name
                values["Age"] = age
                values["Email"] = email
                userlist.append(values)
                break

        print('--'*40)
        choice = input('Do you want enter more values : Y | N : ')
        if choice.lower() in ['n','no']:
            break


try:
    user_input()
except InvalidAge as e:
    print(e.error_message)


print('User Entered Values : ',userlist)

import sys
sys.exit(0)


class Account:

    def __init__(self,accnum,acctype,bal):
        self.account_num = accnum
        self.account_type = acctype
        self.account_balnace = bal

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

    def check_balance(self):
        return self.account_balnace


ac1 = Account(11111,'Saving',5000.30)
ac2 = Account(11112,'Saving',51000.30)
ac1.check_balance() #5k
ac2.check_balance() #51K

value = [1,2,3]
try:
    value[4]=10/0
    #ac1.accounttype  # attribute error --> beconz -> there is no attribute with accounttype --> actual --> account_type ->
except FileNotFoundError as file:
    pass
except IndexError as ind:
    pass
except ValueError:
    pass





userlist = []







