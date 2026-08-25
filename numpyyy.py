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

# PRATice on numpy
# import numpy as np

# marks = np.array([45, 78, 32, 90, 66, 25, 88])

# print(marks)
# print(marks.shape)
# print(marks.size)
# print(marks.mean())
# print(marks.max())
# print(marks.min())
# print(marks+5)

# import numpy as np
# numbers = np.array([10, 20, 30, 40, 50])
# print(numbers.shape)
# print(numbers.size)
# print(numbers.dtype)


# import numpy as np
# sales = np.array([1200, 1500, 800, 2200, 1750, 3000, 950])
# print(np.sum(sales))
# print(np.mean(sales))
# print(np.max(sales))
# print(np.min(sales))
# greater = sales[sales>1500]
# print(greater)

# slicing
# import numpy as np
# data = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# print(data[:3])
# print(data[2:5])
# print(data[:4:-1])
# print(data[::2])
# import numpy as np
# sales = np.array([
#     1200, 1500, 800, 2200,
#     1750, 3000, 950, 2800,
#     1350, 1900
# ])
# print("1 . total sales")
# print("2 . average sales")
# print("3 . maximum sales")
# print("4 . minimum sales")
# print("5 . number of sales is greater 1500 sales")
# print("6 . sales increase by 10 percent sales")
# print("7 . create new array sales is greater than 2000 sales")
# choice = int(input("enter your choice 1,2,3,4,5,6,7 "))
# if (choice==1):
#     print(np.sum(sales))
# elif(choice==2):
#     print(np.mean(sales))
# elif(choice==3):
#     print(np.max(sales))
# elif(choice==4):
#     print(np.min(sales))
# elif(choice==5):
#     greater = sales[sales>1500]
#     print(greater)
# elif(choice==6):
#     increase = sales*1.10
#     print(increase)
# elif(choice == 7):
#     new_array = sales[sales>2000]
#     print(new_array)
# else:
#     print("invalid option")


# import numpy as np

# marks = np.array([
#     [78, 65, 90],
#     [45, 82, 71],
#     [91, 55, 88],
#     [67, 74, 83]
# ])

# print(marks.shape)
# print(marks[0])       # first row
# print(marks[:, 1])    # second column

# print(np.mean(marks, axis=1))  # average of each row
# print(np.mean(marks, axis=0))  # average of each column
# import numpy as np
# marks= np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# print(np.shape(marks))
# print(np.ndim(marks))
# print(np.size(marks))
# print(marks[:,2])
# print(marks[0])
# print(np.sum(marks , axis = 1))
# print(np.mean(marks , axis = 0))

# import numpy as np
# marks = np.array([
#     [78, 65, 90],
#     [45, 82, 71],
#     [91, 55, 88]
# ])
# sum = marks>80  
# # this is for the true or false
# # print(sum)
# print(marks[marks>80])

# small student anlyseer
# import numpy as np
# marks = np.array([
#     [78, 65, 90],
#     [45, 82, 71],
#     [91, 55, 88],
#     [67, 74, 83]
# ])
# # student , subject
# # average marks of every student 
# choice = int (input("enter the choice from 0 to 7  "))
# if choice == 1:
#     print("average marks of each student is")
#     print(np.mean(marks , axis = 1))
# elif choice==2:
#     print("average marks in subjects")
#     print(np.mean(marks, axis =0))
# elif choice==3:
#     print("highest marks")
#     print(np.max(marks))

# elif choice==5:
#     print("marks greater than 80")
#     print(marks[marks>80])
# elif choice==6:
#     print("number of marks greater than 80")
#     print(np.sum(marks>80))
# elif choice==7:
#     print("hieghest avg odf student")
#     avg = np.mean(marks , axis = 1)
#     hiegest = np.max(avg)
#     print(hiegest)