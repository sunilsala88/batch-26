

# #create
# l1=[1,2,3,1,'abc','xyz','amzn',66.55,True,False,0]
# print(len(l1))

# l1.append(True)
# print(l1)

# # l1.clear()
# # print(l1)

# c=l1.count(1)
# print(c)

# l1.extend([5,6,7])
# print(l1)

# i1=l1.index('xyz')
# print(i1)

# l1.insert(1,'tsla')
# print(l1)

# v1=l1.pop(1)
# del l1[1]

# print(l1)

# l1.reverse()
# print(l1)

# l3=[5,4,7,3]
# l3.sort()
# print(l3)



# str1='hello'
# str1=str1.replace('e','a')
# print(str1)


# #hello
# ['h','hello','o']
# # a=input('type something')
# # answer=[a[0],a,a[-1]]
# # print(answer)


# b=[55,66,77,88]
# b[0]=99
# print(b[1:])
# del b[1:-1]
# print(b)


# #tuple
# t1=(55,66,77,66)
# c1=t1.count(66)
# print(c1)

# #dictionary

# d1={'amzn':500,'tsla':600,'goog':700}
# print(d1)
# print(len(d1))

# print(d1['goog'])

# #new elem
# d1['nifty']=900
# print(d1)

# #update
# d1['tsla']=1000
# print(d1)

# print(d1['tsla'])
# v1=d1.get('ongc')
# print(v1)

# # #python
# # {'pyt':'hon'}
# # value1=input('enter something')
# # d1={}
# # #dic_name[key]=value
# # d1[ value1[:len(value1)//2] ]=value1[len(value1)//2:]
# # print(d1)

# # name=input('enter stock name')
# # price=int(input('enter stock price'))
# # dit1={}
# # dit1[name]=price
# # print(dit1)

# # dit1.fromkeys([1,2,3],66)
# # print(dit1)

# print(list(d1.keys()))
# print(list(d1.values()))
# print(list(d1.items()))



# #set
# s1={5,6,7}
# s2={1,2,3}
# print(type(s1))
# print(s1)

# s3=s1.union(s2)
# print(s3)

# str1='hello'


# variable1={66}
# print(type(variable1))

# if variable1:
#     print('truthy')
# else:
#     print('falsy')

# dict1={'amzn':600,'tsla':700}
# result=dict1.get('tsla')

# if result:
#     print(result)
# else:
#     print('it doesnt exist')


# # number=input('enter a number')
# # #0->print ends with zeor
# # #else -> print number
# # if number[-1]=='0':
# #     print('ends wiht zero')
# # else:
# #     print(number)



# #list of list
# ln=[ [11,22,33] , [44,55,66] , [77,88,99] ]
# print(ln[2][1])

# #dict of list

# dc1={
#     'amzn':[33,44,55,66] ,
#     'tsla':[99,22,33]
# }

# # v=dc1.get('tsla')[1]
# v=dc1['tsla'][1]
# print(v)





# #dict of list
# stock_sector={
#     "tech":[ {'tcs':[44,55]} , 'infy' , 'wipro' ] ,
#     'fmcg':['tata','dmart','nstle'],
#     'bank':['kotak','hdfc','icici']
# }

# answer=stock_sector['tech'][0]['tcs'][1]
# answer=stock_sector.get('tech')[0].get('tcs')[1]
# print(answer)



a,b,c=(1,2,3)
print(a)

b1,b2,b3=[1,2,3]
print(b1)

s1={44,55,66}
s1.add('33')
print(s1)

portfolio1 = {"AAPL": 100, "MSFT": 150}
portfolio2 = {"GOOGL": 200, "AMZN": 250}
portfolio1.update(portfolio2)
print(portfolio1)