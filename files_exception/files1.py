


#
# f1=open('files_exception/first2.txt','w')
# f1.write('this is first line \n')
# f1.write('this is my 2nd line')
# f1.close()

# with open('files_exception/data.txt','w') as f2:
#     f2.write('stock name')



# r1=open('/Users/algotrading2024/batch 26/loops/hello1.txt','r')
# data=r1.read()
# print(data)
# r1.close()

# with open('data2.txt','r') as r2:
#     data=r2.read()
# print(data)


# with open('/Users/algotrading2024/batch 26/loops/hello1.txt','a') as t1:
#     t1.write('\nstock name')



# with open('file1.txt','r') as r1:
#     n=r1.read()
#     n=int(n)

# with open('file2.txt','w') as w2:
#     w2.write(str(n**2))


# stock_prices={'amzn':55,'tsla':700,'goog':600}

# with open('data3.txt','a') as t2:
#     for i,j in stock_prices.items():
#         t2.write(i+":"+str(j)+'\n')



stock_prices={'amzn':500,'goog':600,'tsla':900,'nifty':50}

portfolio={}
total=0
while True:
    name=input('enter the name of stock')
    if name.upper()=='Q':
        break
    if name=='nifty':
        print('you cannot buy this stock try some other stock')
        continue
    found=stock_prices.get(name)
    if found:
        portfolio[name]=found
        total=total+found
    else:
        print('this stock doesnt exist')
    

print(total)
portfolio['total']=total
print(portfolio)


with open('data4.txt','a') as t2:
    for i,j in portfolio.items():
        t2.write(i+":"+str(j)+'\n')