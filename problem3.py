# ============================================================
# PROBLEM 3: Take 5 numbers and count Positive, Negative, Zero
# ============================================================

nums = []

for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    nums.append(num)

positive = 0
negative = 0
zero = 0

for n in nums:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

print("\n--- Results ---")
print("Numbers entered:", nums)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeroes:", zero)