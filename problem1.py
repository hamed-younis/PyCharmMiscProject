# Take 10 numbers from the user in a list and find:
# Sum
# Average
# Largest number
# Smallest number



numbers = []

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

print("\n----- Results -----")
print("numbers enterd:", numbers)
print("sum:", total)
print("average:", average)
print("largest:", largest)
print("smallest:", smallest)