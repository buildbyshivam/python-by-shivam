# class student :

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database.")
    

# s1 = student("karan",97)
# print(s1.name,s1.marks)

# s2 = student("mayank",85)
# print(s2.name,s2.marks)
# class student :

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print( self.name,"your avg score is:",sum/3)

# s1 = student("tony stark[94,45,100]")
# s1.get_avg()
# account #
# class Account :
     
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc
#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount,"was debited")
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs",amount,"was credited")
#         print("total balance = ",self.get_balance())

#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(10000,12345)
# # print(acc1.balance)
# # print(acc1.account_no)
# acc1.debit(1000)
# acc1.credit(500)
# class student :
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem +self.math) /3 ) +"%"
    
# stu1 = student(98,97,92)
# print(stu1.percentage)
# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#     def shownumber(self):
#         print(self.real,"i +",self.img,"j")
    
#     def __add__(self,num2):
#         newreal = self.real + num2.real
#         newimg =self.img+ num2.img
#         return complex( newreal,newimg)
    
#     def __sub__(self,num2):
#         newreal = self.real - num2.real
#         newimg = self.img - num2.img
#         return complex(newreal,newimg)
        


# num1 = complex(1,5)
# num1.shownumber()

# num2 = complex(5,7)
# num2.shownumber()

# num3 = num1+num2
# num3.shownumber()

# num4 = num1-num2
# num4.shownumber()
class employee:
    def __init__ (self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        