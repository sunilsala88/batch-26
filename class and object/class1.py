#class is bluprint of object
#object is instance of class
#attribute->any variable created inside class
#class attribute #features that are common for all object
#object/instance attribute #feature that are unique for all object
#mehod -> any function created inside a class
#constructor (__init__) method which is executed when we create a object
#self any method you create inside a class should have self
#if you want to create any instance attribute inside a class you have to use self
#if you want to acces any attribute you have to use self
#oops


class Student:
    dress_code='black-white'
    subjects=['english','maths','science']

    #constructor
    def __init__(self,name,email,phone_no):
        self.name=name
        self.email=email
        self.phone_no=phone_no
    
    def __str__(self):
        return self.email
    
    def about_student(self):
        return f"my name is {self.name} and my email is {self.email}"




s1=Student('vijay','vijay@gmail.com',9999999)
print(s1.dress_code)
print(s1)




# class Cars:
#     wheels=4
#     window='glass'

#     def __init__(self,color,car_type,fuel,transmission):
#         self.color=color
#         self.car_type=car_type
#         self.fuel=fuel
#         self.transmission=transmission

    

# car1=Cars('black','sedan','petrol','manual')
# print(car1.transmission)
# print(car1)


# car2=Cars('red','suv','diesel','amt')
# print(car2.car_type)



# class Broker:
#     stocks={'amzn':500,'goog':900,'tsla':300}
#     news='amzn is good stock'

#     def __init__(self,name,money,id):
#         self.name=name
#         self.wallet=money
#         self.unique_id=id
#         self.portfolio={}
    
#     def buy(self,stock_name):
#         found=self.stocks.get(stock_name)
#         if found:
#             if found<self.wallet:
#                 self.portfolio[stock_name]=self.stocks.get(stock_name)
#                 self.wallet=self.wallet-found
#             else:
#                 print('not enough money')
#         else:
#             print('stock doesnt exist')
    
#     def sell(self,stock_name):
#         if stock_name in self.portfolio.keys():
#             self.wallet=self.wallet+self.portfolio.get(stock_name)
#             del self.portfolio[stock_name]



# trader1=Broker('sunil',1000,578)
# print(trader1.portfolio)
# trader1.buy('amzn')
# trader1.buy('goog')
# print(trader1.portfolio)
# trader1.sell('amzn')
# print(trader1.portfolio)



# # trader2=Broker('matt',2000,579)
# # print(trader2.wallet)
# # print(trader2.portfolio)
        


# class BankAccount:

#     def __init__(self,account_number,initial_balance):
#         self.account_number=account_number
#         self.initial_balance=initial_balance

#     def deposit(self,money):
#         if money>0:
#             self.initial_balance=self.initial_balance+money
#         else:
#             print('invalid money')

#     def withdraw(self,money):
#         if self.initial_balance>money:
#             self.initial_balance=self.initial_balance-money
        
#         else:
#             print('not enough money')
    
#     def get_balance(self):
#         return self.initial_balance





# # Create a new bank account instance
# my_account = BankAccount(account_number="12345678", initial_balance=1000)

# # Deposit and withdraw
# my_account.deposit(500)

# BankAccount.deposit(my_account,500)

# my_account.withdraw(200)
# print(my_account.get_balance())  # Output: 1300
# print(my_account)

