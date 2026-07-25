# movies =[]
# mov1 = input("enter the 1st movie")
# mov2 = input("enter the 2nd movie")
# mov3 = input("enter the 3rd movie")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print (movies)
# palidrome find karne ka
list1= [1,2,3,2,1]
copy_list1= list1.copy()
copy_list1.reverse()
if(copy_list1== list1):
    print("the list is palidrome")
else:
    print("not palidrome")