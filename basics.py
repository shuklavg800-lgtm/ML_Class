import math 


# # # print(53)
# # # # data types
# # # name ="prince"
# # # age= 20

# # # print(type(name))
# # # print(type(age))

# a=10
# b=20
# # print("before a ",a)
# # print("before b ",b)

# # # printting the sum diff etc
# # print("sum ",a+b)
# # print("diff ",a-b)
# # print("prod ",a*b)
# # print("quotient ",a/b) 
# # print("type of quotient : ",type(a/b))
# # # swapping of the variables without using the third variable
# # a=a+b
# # b=a-b
# # a=a-b
# # print("after a ",a)
# # print("after b ",b)

# # print("quotient ",a/b) 
# # print("type of quotient : ",type(a/b))
# # print((a==b))
# # print (not True)
# # print (not False)

# # name =input("enter ur name")
# # print(name,"welcome")

# val =input("enter some value ")
# print("the value is", val, "and the data type is ", type(val))
# # print(val+10) # this will result in TypeError: can only concatenate str (not "int") to str

# # for coverting the val to the int or float we use type casting
# print(type(int(val)))
# val= int(val)
# print("the after type casting value is", val, "and the data type is ", type(val))
# # also we can use int statement in the same line 
# val =int (input("enter some value "))
# print(type(val))
 
#  practice 
# a=int(input("enter the val of a"))
# b=int(input("enter the val of b"))
# # sum=print("the sum of a and b is ",(a+b))
# print(sum(a,b))


# # string functions

# name = input("Enter the name: ")

# # printing the length of the name
# print("length of the name",len(name))
# # Capitalize the first letter
# print("Capitalized:", name.capitalize())

# # Swap case (uppercase ↔ lowercase)
# print("Swapcase:", name.swapcase())

# # Count occurrences of 'o'
# print("Count of 'o':", name.count("o"))

# # Find the index of 'P' (returns -1 if not found)
# print("Find 'P':", name.find("P"))


# conditional statements

# indentation acts as the curly braces of cpp or C on Java, use a tab or 4 spaces

# age=int(input("Enter ur age"))
# if (age>18):
#     print("eligible to vote")
# elif age>16:
#     print("Get ur ids done to be eligible in nexxt 2 yrs")
# else:
#     print("not eligible")


# str="print"
# if (len(str)):
#     print("true")

# a=10
# b=print("prince")
# print(a+b) # returns typeError since the datatype of b is None
 

# marks=int(input("Enter ur marks"))
# if (marks>90):
#   print("A grade")

n=int(input("Enter a number"))
a=1
while a<=10:
    print(a*n)
    a=a+1