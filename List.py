# lists in python similar to arrays in cpp 

# list of list
# student=[["prince",95,'football'],["rajat",90,"football"],["shiv",90,"football"]]
# print(student[0])
# print(student[1])
# print(student[2])

# to take input and store them in the list
# n=int(input("Enter the no of movies"))
# i=n
# list=[]
# while(i>0):
#     list.append(input("Enter the movie name "))
#     i-=1

# print(list)

# to check whether the list contains the palindrome elements or not
n=int(input("Enter the no of elements "))
i=n
list=[]
while(i>0):
    list.append(int(input("Enter the element ")))
    i-=1
print(list)
list_temp =list.copy()
list_temp.reverse()
print(list)
print(list_temp)
if (list_temp==list):
    print("A palindrome list")
else:
    print("not a palindrome")