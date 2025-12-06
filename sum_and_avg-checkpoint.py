numbers = []
for i in range(5):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

total = sum(numbers)
average = total / 5

print("Sum =", total)
print("Average =", average)
