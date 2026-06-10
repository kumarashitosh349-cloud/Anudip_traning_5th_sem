# Accept marks of 5 subjects
total = 0
fail_count = 0

for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    total = total + m
    
    if m < 40:
        fail_count = fail_count + 1

# Calculate percentage
percentage = total / 5

# Decide grade using only if-else
if percentage >= 90:
    grade = "A+"
else:
    if percentage >= 75:
        grade = "A"
    else:
        if percentage >= 60:
            grade = "B"
        else:
            if percentage >= 40:
                grade = "C"
            else:
                grade = "Fail"

# Display result
print("\n--- Result ---")
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Number of subjects failed =", fail_count)