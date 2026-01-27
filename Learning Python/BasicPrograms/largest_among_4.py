a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))
c=int(input("Enter number 3 "))
d=int(input("Enter number 4 "))

if(a>b and a>c and a>d):
    print("largest is ",a)
elif(b>a and b>c and b>d):
    print("largest is ",b)
elif(c>a and c>b and c>d):
    print("largest is ",c)
else:
    print("largest is ",d)