# def func_name(a,b):
#     s=a+b
#     print(s)
#     return s
# func_name(12,15)
# func_name(1,5)
# def func_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg
# func_avg(25,50,75)
# print("shivam",end = " 45 ")
# print("khandelwal")
# cities = ("delhi","jaipur","noida","mumbai")
# heroes =  ("james bond","captain america","thor")

# print(heroes[0],end="\n")
# print(heroes[1],end= "\n ")
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)
# def print_list(list):
#     for item in list:
#         print(item,end =" ")
# print_list(cities)
# def calc_fac(n):
#     fac = 1
#     for i in range(1,n+1):
#         fac*=i
#         print(fac)
# calc_fac(6)
# def converter(usd_value):
#     inr_value = usd_value*83
#     print(usd_value,"USD" , inr_value,"INR")
# converter(12)

# def check_nums(n):
#     even = (n%2==0)
#     if  even:
#         print("n is even")
#     else:
#         print("n is odd")

# check_nums(25)
# check_nums(44)

# 12 04 2026
# def add(n):
#     print(n*n)
# add(3)
# def number(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# number(5)
# def numbers(a,b):
#     if a>b:
#         print("a is maximum")
#     else:
#         print("b is maximum")
# a = int(input("enter the first number"))
# b= int(input("enter the second number"))
# numbers(a,b)
# def fact(n):
    
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# n = int(input("enter the number"))
# fact(n)

# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
    
#     return True
# n = int (input("enter the number"))
# if is_prime(n) :
#        print("prime number")
# else:
#        print("not prime")
# def rev_string(str):
#     return str[::-1]

# str = "hello"
# rev_string(str)
# print(rev_string(str))


# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0 
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# s ="helloindia"
# print(count_vowels(s)-

# def sum_list(lst):
#     total = 0
#     for num in lst:
#         total+=num
#     return total
# numbers = [45,4,9,89]
# print(sum_list(numbers))