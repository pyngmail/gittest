import numpy as np

arr=np.zeros((10,10))
arr[0::2,1::2]=1
print(arr)
# 2-d list (list of lists) -> 2-d array
a = np.array( [[1., 2., 3.], # row:0   #橫 row 直 column
               [4., 5., 6.]] ) # row:1
print(a)
print(a.size)
print(a.ndim)    #維度
print(a.T)
print(a.itemsize)
print(a.shape)
print(a.strides)
print(a.dtype)
li=a.tolist()  #轉成list
print(type(li))

b=np.arange(24).reshape(4,6)
print(b)
