# a='2024-02-25'

# #samay


# class samay:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
#         if self.month>12 or self.month<0:
#             print("invalid month")
        
#     def __str__(self):
#         return f"{self.year}-{self.month}-{self.day}"
    
#     def add_days(self,n):
#         self.day=self.day+n
    
#     def get_month(self):
#         return self.month
    



# #what is self in class


# d1=samay(2024,11,25)
# print(d1)
# d1.add_days(10)
# print(d1)

# d2=samay(2024, 13, 25)
# print(d2)


#import datetime
import datetime as dt

d1=dt.datetime(2024, 7, 13 ,5,15,30)
print(d1.month)
#0 monday
#1 tuesday
#6 sunday