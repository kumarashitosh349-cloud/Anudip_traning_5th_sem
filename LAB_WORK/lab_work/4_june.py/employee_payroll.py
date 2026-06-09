name = input("Enter name: ")
basic = int(input("Enter salary: "))

hra = basic * 0.2
da = basic * 0.1
pf = basic * 0.12

gross = basic + hra + da
net = gross - pf

if net > 50000:
    grade = "Senior Grade"
elif net > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

print("Gross Salary:", gross)
print("Net Salary:", net)
print("Grade:", grade)