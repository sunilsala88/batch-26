
# stock_prices={'amzn':500,'goog':600,'tsla':900}


# portfolio=[]
# while True:
#     input_name=input('enter the stock name (press Q to stop)')
#     if input_name.upper()=='Q':
#         break
    
#     found=stock_prices.get(input_name)
#     if found:
#         portfolio.append(input_name)
#     else:
#         print('name doesnt exist')

# print(portfolio)


current_money=500
target=10000
monthy_saving=500
interest=0.05
month=1
while True:


    current_money=current_money+500+ ((0.05/12)*current_money)
    print(current_money)
    if current_money>=target:
        break
    month=month+1

print(month)