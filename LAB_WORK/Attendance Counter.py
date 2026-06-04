present = 0
absent = 0

n = int(input("Enter number of students: "))

for i in range(n):
    status = input(f"Student {i+1} (P/A): ").upper()

    if status == "P":
        present += 1
    elif status == "A":
        absent += 1

print("Present:", present)
print("Absent:", absent)