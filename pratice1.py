# name = "Shivam"
# age = 18
# dreamjob = "work at google"
# location = "India"
# print(f"My name is {name} My age is{age} my dream job is{dreamjob} I live in {location}")
# num1 = int(input("enter the  first number a :"))
# num2 = int(input ("enter the second number b :"))

# intsum = int(num1)+int(num2)
# print(f"sum of the two number is {intsum} ")
# num1 = 5
# num2= 3
# sum = num1+num2
# sub = num1-num2
# mul = num1*num2
# division = num1/num2
# print(f"sum of two number{sum},sub for two number is {sub},mul of two number{mul},division of two number{division}")

# if else statement
# a = int(input("enter the number "))
# if a%2==0:
#     print("the given number is even")
# else :
#     print("the given number is odd")

# grade system
# a = float(input("enter the grade of student"))
# if a>=90:
#     print("you are outstanding take A grade")
# elif a>=80:
#     print("you are excellent take B grade")
# elif a>=70:
#     print("you are good take C grade")
# elif a>=60:
#     print("you take D grade")
# elif a>=36:
#     print("you take E grade")
# else:
#     print("you are fail")
 # loops for 
# for i in range(1,11):
#     if i%2 ==0:
#         print(i,"even")
#     else:
#         print(i,"odd")
# while loop 
# i=10
# while i>=1:
#     print(i)
#     i-=1
# lists
# marks = [97,45,87]
# print(marks[0])
# print(marks[-1])
# marks.append(85)
# print(len(marks))
# marks.pop()
# print(marks)
# if 97 in marks:
#     print("yes")
# else:
#     print("no")
# print(marks[0:])
# print(marks[:0])

# loops more pratice
# for i in range(1,21):
#     print(i)
# i=20
# while i>=1:
#     print(i)
    
#     i-=1
# for i in  range (1,31,2):
#     print(i)
# a= int(input("enter the multiple table"))
# for i in  range (1,11):

#  print(f"{a}x{i}= {i*a}")
# total=0
# for i in range(1,101):
#     total+=i
   
# print(total)
#    for reverse the number
# reversenumber = 0
# a = int(input("enter the digit"))
# originalnumber=a
# while a>0:
#    digit = a%10
#    reversenumber=reversenumber*10+digit
#    a=a//10
# if reversenumber==originalnumber:
#     print("number is the palidrome")
# else:
#     print("not palidrome")
# pattern
# for i in range (1,6):
#     for j in range(i+5):
#         print(j,end="")
#     print()
# for i in range (1,6):
#     print("*"*i)
# rows = 5

# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2*i - 1))
# rows = 3

# for i in range(1, rows + 1):
#     spaces = rows - i
#     stars = 2*i - 1
#     print(" " * spaces + "*" * stars)
# rows =5
# for i  in range (1,rows + 1):
#     spaces = rows-i
#     stars = 2*i-1
#     print(" " *spaces + "*" * stars)
# rows  = 4
# for i in range(1,rows+1):
#     print()
# rows = 4
# for i in range(rows,0,-1):
#     print(" "*(rows-1)+"*" * (2*i-1))
# for i in range(2):
#     for j in range(3):
#         print(i,j)
# nested loops concept
# for i in range(1,4):
#     for j in range(i):
#         print("*",end = "")
#     print()
# for i in range(3):
#     print("*"*3)
# for i in range(1,4):
#     print("*"*i)
# for i in range(3,0,-1):
#     print("*"*i)
# print("done")
# functions ///////////
# def add(a,b):
#     print(a+b)
# add(5,3)
# def multiplication(a,b):
#     return a*b
# x=multiplication(3,4)
# print(x)
# def add(a,b):
#     return a+b
# x=add(2,3)+add(4,6)
# print(x)
# def double(x):
#     return x * 2

# def square(x):
#     return x*x
# def add(a,b):
#     return a+b
# print(square(add(3,4)))
# def add(a,b):
#     return a+b
# x =1
# for i in range(3):
#     x = add(x,2)
# print(x)


# print(double(3) + double(4))
# lists.......
# numbers = [4,5,6,7,8]
# print(numbers[-1])
# numbers = [2,4,6]
# for n in numbers:
#     print(n*n)
# numbers = [1, 2, 3]
# dictionary...........

# total = 0

# for n in numbers:
#     total = total + n

# print(total)
# numbers=[4,6,5]
# total =0
# for i in numbers :
#     total = total+i
# print(total)
# numbers = [10,20,30]
# numbers.append(40)
# numbers.remove(20)
# numbers.pop()
# print(numbers)
# dictionary.....////
# student = {
#    " name":"shivam",
#    "age":20

# }
# print(student["age"])
# marks = {
#     "maths":94,
#     "science":97
# }
# for subjects in marks:
#     print(subject)

# exception handling 
# a = int(input("enter the number for multiplication"))
# print(f"multiplication of {a} is :")
# try:
#   for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except  Exception as e :
#   print("wher are you ")
# oops programming
# class Student :

#    def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#    s1 = Student("shivam",20)
#    print(s1.name)
# class student:
# #     def__init
# def fact(n):
#     if  n<0:
#         return "not defined for the negative number"

    
#     result = 1
#     for i in range(1,n+1):
#         result*=i

#     return result
# n = int(input('enter the vslue you wsnt to fsctorial'))
# fact = 1 
# for i in range (1,n+1):
#     fact*=i
# print(fact)

# # list and dictionary
# numbers = [12, 45, 7, 23, 56, 89, 34, 10]
# max_number = numbers[0]
# /max number
# for num in numbers[1::]:
    
#     if num > max_number:
#         max_number = num
# print(max_number)
# min number
# min_number = numbers[0]
# for num in numbers[1:]:
#     if num < min_number:
#         min_number = num
# print(min_number)
# average number

# sum = numbers[0] +numbers[1] + numbers[2] +numbers[3] + numbers[4] +numbers[5] +numbers[6] +numbers[7]
# average_number = sum / len(numbers)
# print(average_number)
# for num in numbers:
# total+=num
# average = total / len(numbers)
# for num in numbers[1:]:
#     if num > 30:
#         print(num)

# numbers = [ 10,20 ,10 ,30,20,40,50,30]
# unique_number = []
# for num in numbers:
#     if num not in unique_number:
#         unique_number.append(num)
# print(unique_number)

# students = {
#     "Rahul": 78,
#     "Aman": 92,
#     "Priya": 85,
#     "Riya": 67,
#     "Karan": 91
# }
# print(max(students.keys()))
# for students , marks in students.items():
#     print(students ,marks)
# highest_student = ""
# highest_marks =0

# for name , marks in students.items():
#     if marks > highest_marks:
#         highest_marks = marks
#         highest_student = name
# print(highest_student)
# print(highest_marks)
# lowest_student =""
# lowest_marks = 0
# for name , marks in students.items():
#     if marks < lowest_marks:
#         lowest_marks = marks
#         lowest_student = name
# print(lowest_marks)
# print(lowest_student)

# average 
# sum = 0
# average_score = 0
# for name , marks in students.items():
#     sum+=marks
#     average_score = sum / len(students)
    
# print(average_score)

# student scoring above 80:

# for name , marks in students.items():
#     if marks > 80:
#         print(name , marks)


numbers = [10, 20, 30, 40, 50]
def calculate_statics(numbers):
    print("1 . max m, 2. for min , 3.for average"  )
    choice = int(input("enter the choice"))
    if choice==1:
        max_number = numbers[0]
        for num in numbers[1:]:
           if num > max_number :
             max_number = num
        print(max_number)
        
    elif choice==2:
      min_number = numbers[0]
      for num in numbers[1:]:
           if num < min_number:
            min_number = num
      print(min_number)
    else:
        total = 0
        average =0
        for num in numbers:
            total+=num
            average = total/len(numbers)
        print(average)

calculate_statics(numbers) 