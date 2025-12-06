a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (a > b and a < c) or (a > c and a < b):
    second = a
elif (b > a and b < c) or (b > c and b < a):
    second = b
else:
    second = c

print("Second largest number =", second)
