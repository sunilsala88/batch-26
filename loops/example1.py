

# list1=[44,5,7,55,99]
# list2=['amzn','tsla','goog']

#iteration / looping
#iterable / datatype on which you can use a loop



# for i in list1:
#     if i%2==0:
#         print(i,'even')
#     else:
#         print(i,'odd')

# #type 1
# for name in list2:
#     print(name)




# a=[100]

# for i in a:
#     print(i)

# #keywords
# list,dict,int,float,bool




# prices=[33,44,55,66]

# total=0
# for price in prices:
#     print(price)
#     total=total+price
# print(total)


# a=list(range(100))
# print(a)

stocks=['amzn','tsla','google','nifty']

#type 2 for loop 
for ind in range(len(stocks)):
    print(stocks[ind])


#create a list of first 100 even numbers
even=[]
for i in range(200):
    if i%2==0:
        even.append(i)
print(even)


stock_prices=[120, 11, 130, 140, 150,99]
# high=120

# for i in stock_prices:
#     if high>i:
#         high=i
# print(high)

# n=3
# final_list=[0,0]
# for i in range(len(stock_prices)):
#     if i>=2:
#         final_list.append((stock_prices[i]+stock_prices[i-1]+stock_prices[i-2])/3)
# print(final_list)


count=0
average=sum(stock_prices)/len(stock_prices)
print(average)
for price in stock_prices:
    if price>average:
        count=count+1
print(count)




stock_prices=[44,55,66,77,88]
final_list=[0,0,0]
for i in range(len(stock_prices)):
    if i>=3:
        av1=(stock_prices[i]+stock_prices[i-1]+stock_prices[i-2])/3
        final_list.append(av1)
print(final_list)