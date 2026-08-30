# add two number
# num1 = int(input("enter the first number"))
# num2 = int (input("enter the second number"))
# sum = num1 + num2
# print(sum)

# import operator
# print(operator.add(5,6))
# import math
# num = [6,6]
# print(math.fsum(num))
#
# maximum of two number
# num1 = int(input("enter the first number"))
# num2 = int (input("enter the second number"))
# if(num1>num2):
#     print("num1 is greatest among two",num1)
# else:
#      print("num2 is greatest among two",num2)
# a =5
# b = 7
# print(max(a ,b))
# find factorial of number
# import math
# print(math.factorial(6))
# import numpy as np
# n= 6
# if n>=0:
#     print(np.prod(range(1,n+1)))
# else:
#     print("factorial is not defiend")
# n=6
# f =1 
# if n<0:
#     print("fact is not defined")
# else:
#     for i in range(1,n+1):
#         f*=i
#         print(f)

# check armstrong number
num1 = int(input("enter the number"))
sum = 0
digit = len(str(num1))
num = num1
while num > 0:
    num = digit % 10
    sum += digit**digit
    num//= 10
if (sum==num):
    print("armstrong nuber")
else:
    print("not armstrong number")