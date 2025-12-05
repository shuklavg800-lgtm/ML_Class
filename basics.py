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
a=int(input("enter the val of a"))
b=int(input("enter the val of b"))
# sum=print("the sum of a and b is ",(a+b))
print(sum(a,b))
