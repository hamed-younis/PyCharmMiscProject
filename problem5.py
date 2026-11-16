# Create two lists of numbers and make a new list that stores the addition of both lists element by element






list1 = []
list2 = []

print("Enter 5 numbers for List 1:")
for i in range(1, 6):
    num = float(input(f"  List1 - Number {i}: "))
    list1.append(num)

print("Enter 5 numbers for List 2:")
for i in range(1, 6):
    num = float(input(f"  List2 - Number {i}: "))
    list2.append(num)

result_list = []

for i in range(5):
    result_list.append(list1[i] + list2[i])

print("\n--- Results ---")
print("List 1:", list1)
print("List 2:", list2)
print("Sum List:", result_list)