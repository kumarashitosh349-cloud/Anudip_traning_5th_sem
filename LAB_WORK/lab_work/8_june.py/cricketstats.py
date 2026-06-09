runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

more_500 = []
below_400 = []
total = 0
count = 0

top = ""
low = ""
max_r = 0
min_r = 9999

for p in runs:
    r = runs[p]

    total = total + r

    if r > 500:
        more_500.append(p)

    if r < 400:
        below_400.append(p)

    if r >= 400 and r <= 600:
        count = count + 1

    if r > max_r:
        max_r = r
        top = p

    if r < min_r:
        min_r = r
        low = p

print(more_500)
print(top)
print(low)
print(total)
print(below_400)
print(count)