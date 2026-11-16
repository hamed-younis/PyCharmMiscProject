# Create a list of numbers from 1 to 20 using a loop and print only even numbers.
# Take 5 numbers in a list from the user and count:
# Positive numbers
# Negative numbers
# Zeroes


even_numbers = []

for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers from 1 to 20:")
print(even_numbers)