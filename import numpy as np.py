# import numpy as np
# arr = np.array([2,4,5,6,7])
# print(arr)
# import as a ones
# import numpy as np
# arr_ones = np.ones((2,3))
# print(arr_ones)

# full(shape,value)
# import  numpy as np
# filled_arr = np.full((2,2),7)

# creating sequence of number

# import numpy as np
# arr = np.array([2,4,5,6,7])
# int_arr = arr.astype(int)
# print(int_arr)
# print(int_arr.dtype)

# import numpy as np
# arr = np.array([2,4,5,6,7])
# print(np.sum(arr))
# print(np.mean(arr) )
# print(np.max(arr))
# print(np.min(arr))
# print(np.var(arr))
#indexing and slicing/// 
# import numpy as np
# arr = np.array([2,4,5,6,7])
# print(arr[::-1])
# print(arr[:5])
# print(arr[[1,2,4]])
# print(arr[arr>3])

# reshaping and manipulation
"""
reshape(rows,columns)
"""
# import numpy as np
# arr = np.array([2,4,5,6,7,8])
# reshape_arr = arr.reshape(2,3)
# print(reshape_arr)


"""
flatten


"""
# import numpy as np
# arr = np.array([1,2,3],[4,5,6])
# print(arr.ravel())
# print(arr.flatten())

"""
np.insert(array,index,value,asix=none)
"""
# import numpy as np
# arr =np.array([10,20,30,40,50])
# new_arr = np.insert(arr,2,100)
# print(new_arr)

# import numpy as np
# arr_2d = np.array([1,2],[3,4])
# newarr_2d = np.insert(arr_2d,1,[5,6],axis=1)
# print(newarr_2d)

# import numpy as np
# arr = np.array([10,20,30])
# new_arr = np.append(arr,[60,50,40])
# print(new_arr)

# import  numpy as np
# arr1 = [1,2,3]
# arr2 = [4,5,6]
# new_arr = np.concatenate((arr1,arr2))
# print(new_arr)

# import numpy as np
# arr = np.array([1,2,3,4])
# new_arr = np.delete(arr,0)
# new_arr = np.split(arr,2)
# print(new_arr)

# broadcasting
# prices = [10,20,30]
# discount = 10
# final_price = []
# for price in prices:
#     discounted_price = price - (price * discount/100)
#     final_price.append(discounted_price)
    
# print(final_price)

# import numpy as np
# prices = np.array([100,220,300])
# discount = 10
# final_price = prices - (prices*discount/100)
# print(final_price)

# import numpy as np 
# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# result = arr1 + arr2
# print(result)
# import numpy as np
# arr1 = np.array([1,23,4,5,6,7,8,9])
# print(arr1)

# import numpy as np
# arr_3d =np.array([[0,0,0],[0,0,0],[0,0,0]])
# print(arr_3d)
# import numpy as np
# arr = np.arange(2,21,2)
# print(arr)

""" to make identity matrix
"""
# import numpy as np
# arr_4d = np.eye(4)
# print(arr_4d)

# import numpy as np
# arr = np.array([1,2,45],
#                 [5,54,47],
#                 [4,58,65])
# # for i in arr_2d :
# #     if i>=5:
# #         print(i)
# result = arr[arr>5]
# print(result)

