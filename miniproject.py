# calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return ("cannot divide")
    return a/b

num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

print("choose operation")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.division")

choose = input("enter operation 1/2/3/4  ")

if choose=="1":
    print("result:",add(num1,num2))

elif choose=="2":
    print("result:",sub(num1,num2))
elif choose=="3":
    print("result:",multiply(num1,num2))
    
elif choose=="4":
    print("result:",divide(num1,num2))
else:
    print("invalid error")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return("cannot divide")
    return a/b

num1 = float(input("enter the first value"))
num2 = float(input("enter the second value"))

print("choose operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.divide")
choice = int(input("choose operation 1/2/3/4"))

if choice==1:
    print("result:",add(num1,num2))

elif choice==2:
    print("result:",sub(num1,num2))
elif choice==3:
    print("result:",mul(num1,num2))
elif choice == 4:
    print("result:", divide(num1,num2))
else:
    print("invalid number ")