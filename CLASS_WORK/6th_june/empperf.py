employees = (
     ("E101", "Anuj", 92),
     ("E102", "Rahul", 76),
     ("E103", "Priya", 58),
     ("E104", "Neha", 88),
     ("E105", "Amit", 45)
)
#score above 80
for e in employees:
    if e[2] >= 80:
        print(e)

#above 60 need improvement
c = 0
for e in employees:
    if e[2] < 60:
        c += 1
print(c)

#with highest score
h = employees[0]
for e in employees:
 if e[2] > h[2]:
        h = e
print(h)

#list containing name of employees scoring abive 75
names = []
for e in employees:
 if e[2] > 75:
     names.append(e[1])
print(names)


#90and abive=excellent,75-89=good,60-74=average,below 60=needs improvment
for e in employees:
    s = e[2]
    if s >= 90:
        print(e[1], "Excellent")
    elif s >= 75:
        print(e[1], "Good")
    elif s >= 60:
        print(e[1], "Average")
    else:
        print(e[1], "Needs Improvement")

