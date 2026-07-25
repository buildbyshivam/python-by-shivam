# secret = 7
# guess = 0
# while guess!=secret:
#     guess = int(input("enter the guess number"))

#     if guess==secret:
#         print("you are win")
#     else:
#         print("try again")

# secret = 7
# guess = 0
# attempts =0
# while attempts<3:
#     guess = int(input("enter the guess number"))
#     attempts+=1
#     if guess==secret:
#         print("you are win")
        
#         break
#     else:
#         print("try again")
#     if attempts==3 and guess!=secret:
#         print("game over")
# import random
# secret = random.randint(1,10)
# attempts =0
# while attempts<3:
#     guess = int(input("enter the guess number between 1 to 10  "))
#     attempts+=1
#     if guess==secret:
#         print("you win")
#         break
#     elif guess<secret:
#         print("you are too low")
#     else :
#         print("you are too high")
         
# if guess!=secret and attempts==3:

#         print("game over ")
#         print("the correct number is",secret)
# import random 
# secret = random.randint(1,10)
# attempts =3
# print("guess the number from 1 to 10")
# for i in range(attempts):
#     guess = int(input("enter the guess"))
#     if guess==secret:
#         print("you win")
#         break
#     elif guess>secret:
#         print("you are too high")
#     else:
#         print("you are too low")
#     if guess !=secret:
#         print("you lose the game")
# import random
# secret = random.randint(1,10)
# attempts = 3 
# print("guess the number from 1 to 10")
# for i in range(attempts):
#     guess = int(input("enter the guess number"))
#     if guess==secret:
#       print("you win")
#       break
#     elif guess>secret:
#        print('you are too high')
#     else:
#        print("you are too low")
   
# else:
#    print("you lose the game")
import random
secret = random.randint(1,100)
attempts = 6
# guess = int(input("enter the guess number"))
print("guess the number between1 to 100")
for i in range(attempts):
    guess = int(input("enter the guess nnumber"))
    if guess==secret:
        print("you win the game")
        break
    elif guess<secret:
        print("you are too low")
    else:
        print("you are too high")
    
else:
    print("you are lose")

print("randomvalue",secret )