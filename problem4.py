
# Create a program that stores marks of 5 students in a list and calculates:
# Total marks
# Percentage
# Highest marks


marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks of student {i} (out of 100): "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100   # 5 students x 100 max
highest_marks = max(marks)

print("\n--- Results ---")
print("Marks list:", marks)
print("Total marks:", total_marks)
print("Percentage:", percentage, "%")
print("Highest marks:", highest_marks)