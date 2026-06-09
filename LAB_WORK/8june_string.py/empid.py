emp_id = "EMP2026ANUJ458"

u = sum(1 for i in emp_id if i.isupper())
d = sum(1 for i in emp_id if i.isdigit())

year = emp_id[3:7]
name = emp_id[7:-3]

valid = emp_id.startswith("EMP") and year.isdigit() and emp_id[-3:].isdigit()

digits = [int(i) for i in emp_id if i.isdigit()]
total = sum(digits)

print(u)
print(d)
print(year)
print( name)
print(digits)
print( total)
print("VALID" if valid else "INVALID")