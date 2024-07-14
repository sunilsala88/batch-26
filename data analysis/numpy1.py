# #list
# l1=[1,2,3,True]
# print(l1)
# print(type(l1))

# l2=[ [1,2,3] , [4,5,6] ]
# print(l2)
# #numpy
# import numpy as np
# np1=np.array(l1)
# print(np1)
# print(type(np1))

# np2=np.array(l2)
# print(np2)


# l3=[[1,2,3],[4,5,6],[7,8,9]]
# print(l3)
import numpy as np
# np3=np.array(l3)
# print(np3)

# val=np3[2][2]
# print(val)

# val2=np3[1,0]
# print(val2)

np2=np.array([[11,22,33],[44,55,66],[77,88,99]])
print(np2)


print(np2[[0,1,2] , [0,1,2] ])
print(np2[[0,1,2] , [2,1,0] ])

print(np.ones(5,dtype=int))

print(np.arange(9).reshape(3,3))

import numpy as np
#3 by 3 matrix using arange method
print(np.arange(9).reshape(3,3))

#3 by 3 matrix using random method
print(np.random.randint(20,30,size=(3,3)))