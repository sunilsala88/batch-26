
prices=[44,55,66,77]
str1='hello'

#type 1
for p in str1:
    print(p,end='\n')

#type 2
for i in range(10):
    print('hello')


#type 3
for i in range(len(prices)):
    print(prices[i])



# init_money=0
# target=10000
# monthy_saving=500
# interest=0.05



#type 4
dict1={'amzn':500,'goog':600,'tsla':900}
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

#type 4
for key,value in dict1.items():
    print(key,value)




names=['goog','tsla','amzn']
prices=[66,77,88]

final={}
f=len(names)-1
for i in range(len(names)):
    k=names[i]
    v=prices[f-i]
    final[k]=v
print(final)

# list1=[]
# number=2
# while True:
#     list1.append(number)
#     if number==200:
#         break
#     number=number+2
# print(list1)

intl=[1,2,3,4,5,6,7,8,9,10]
index1=0
while True:
    if index1==len(intl):
        break
    if intl[index1]%2==0:
      print(intl[index1])
    index1=index1+1