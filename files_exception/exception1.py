
# num1=input('enter a number')
# num2=input('enter a number')
# print(int(num1)/int(num2))

# try:
#     num1=input('enter a number')
#     num2=input('enter a number')
#     print(int(num1)/int(num2))
# except Exception as e:
#     print('you have done something wrong')
#     print(e)

# print('important')
# a=[2,3,4]
# print(a[5])


#ZeroDivisionError: division by zero
#TypeError: unsupported operand type(s) for /: 'int' and 'str'
#ValueError: invalid literal for int() with base 10: 'a'
#IndexError: list index out of range





try:
    num1=input('enter a number')
    num2=input('enter a number')
    print(int(num1)/int(num2))
except ZeroDivisionError:
    print('zero is not allowed')
except ValueError:
    print('alphabets are not allowed')
