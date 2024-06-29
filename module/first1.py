#module ,package ,library


import random
import time
import sys
import pandas
import numpy
import selenium
import os

print(os.getcwd())

b=pandas.DataFrame()
a=random.random()
print('first line')
time.sleep(2)
print('second line')

# sys.exit()

l1=[]
for i in range(10):
    b=random.randint(10,100)
    l1.append(b)
print(l1)

#take input from user to type a number
#if user type number 50 exit and not print anything
#if user types q break the loop and print entire list
# new_list=[]
# while True:
#     num=input('enter a number')
    
#     if num=='50':
#         sys.exit()
#     if num=='q':
#         break
#     new_list.append(int(num))

# print(new_list)