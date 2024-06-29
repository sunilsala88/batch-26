
#type 1
list1=[22,3,4]
for i in list1:
    print(i)

#type 2
for i in range(10):
    print('hello')

#type 3
for i in range(len(list1)):
    print(list1[i])

#type 4
dict1={'amzn':100,'goog':500,'tsla':590}
for i,j in dict1.items():
    print(i,j)

#while loop
number=1
while True:
    if number==1000:
        break
    number=number+1
    if number==998:
        continue
    print(number)


name='fessorpro'
new=''
for i in name:
    new=i+new
print(new)

l=list(range(-1,-(len(name)+1),-1))
ans=''
for i in l:
    ans=ans+name[i]
print(ans)
