
def average(l1:list) -> float:

    total=0
    for i in l1:
        total=total+i
    average=total/len(l1)


    return average

# ans=average([5,6,7,8,9])
# print(ans)



#2 int return square of both numbers


def rev_string(name):
    rev_name=''
    for i in name:
        rev_name=i+rev_name
    return rev_name

ans=rev_string('sunil')
print(ans)

ans=rev_string('fessorpro')
print(ans)


def calc_len(string_name):
    l=0
    for i in string_name:
        l=l+1
    return l

length=calc_len('sunil')
print(length)


def calculate_sum(num1,num2):
    ans=num1**2+num2**2
    return ans

a=calculate_sum(2,3)
print(a)


def factorial(number):
    fact=1
    for i in range(2,number+1):
        fact=fact*i
    return fact

ans=factorial(5)
print(ans)

def highest(list1):
    greatest=list1[0]
    for i in list1:
        if greatest<i:
            greatest=i
    return greatest

a=highest([44,66,77,22,99])
print(a)