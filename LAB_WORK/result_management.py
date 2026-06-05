total = 0
fail = 0

for i in range(5):
    m = int(input())
    total += m
    if m < 40:
        fail += 1

per = total / 5

if per >= 90:
    grade = "A+"
elif per >= 75:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 40:
    grade = "C"
else:
    grade = "Fail"

print(total, per, grade, fail)