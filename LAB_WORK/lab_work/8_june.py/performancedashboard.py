performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

above_80 = []
excellent = []
good = []
average = []
poor = []

total = 0
count_low = 0

top_emp = ""
top_score = 0

for emp in performance:
    score = performance[emp]

    total = total + score

    if score > 80:
        above_80.append(emp)

    if score < 60:
        count_low = count_low + 1

    if score > top_score:
        top_score = score
        top_emp = emp

    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average.append(emp)
    else:
        poor.append(emp)

avg = total / 10

print("Above 80:", above_80)
print("Need improvement:", count_low)
print("Top performer:", top_emp)
print("Average:", avg)
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)