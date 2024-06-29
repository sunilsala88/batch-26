

# def add_number(num1,num2):
#     ans=num1+num2
#     return ans

# a=10
# b=20
# ans=add_number(a,b)
# print(ans)

# def fibonaci_number(n):
#     num1=0
#     num2=1
#     fibonaci=[num1,num2]

#     for i in range(n-2):
#         current_num=num1+num2
#         fibonaci.append(current_num)
#         num1=num2
#         num2=current_num

#     return fibonaci

# f=fibonaci_number(100)
# print(f)

#local var and global var


# def average(numbers):
#     global a
#     total=0
#     for i in numbers:
#         total=total+i
#     avg=total/len(numbers)
#     a=101
#     print(a)
#     return avg


# def main():
#     n=[5,6,7]
#     print(a)
#     result=average(n)
#     print(a)
#     print(result)

# a=100
# main()
# print(a)


# stock_prices={'amzn':100,'goog':500,'tsla':840}
# def print_stocks():
#     for i,j in stock_prices.items():
#         print(i,j)

# def input_stocks():
#     portfolio={}
#     while True:
#         stock_name=input('enter the stock name(q to quit)')
#         if stock_name=='Q':
#             break
#         found=stock_prices.get(stock_name)
#         if found:
#             portfolio[stock_name]=found
#         else:
#             print('this stock name does not exist type again')

#     return portfolio


# print_stocks()
# p=input_stocks()
# print(p)


def function1(a,b):#9,4
    print(100)
    print(a**2)
    return a+b

def function2(x,y,z): #2,3,4
    b=function1(x,y)#2,3
    print(b)#5
    return b+z #9

def function3():
    a=2
    b=3
    z=4
    a=function2(a,b,z) #9
    b=function1(a,z) #9,4 ->13
    print(a,b)


function3()


#make a function called table (number 5)
#5*1=5
#5*2=10
def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
table(9)