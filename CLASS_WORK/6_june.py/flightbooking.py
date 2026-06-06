bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1
for b in bookings:
    if b[2] == "Confirmed":
        print(b)

# 2
c = 0
for b in bookings:
    if b[1] == "Delhi":
        c += 1
print(c)

# 3
con = wait = can = 0
for b in bookings:
    if b[2] == "Confirmed":
        con += 1
    elif b[2] == "Waiting":
        wait += 1
    else:
        can += 1
print(con, wait, can)

# 4
w = []
for b in bookings:
    if b[2] == "Waiting":
        w.append(b[0])
print(w)

# 5
d = m = ch = 0
for b in bookings:
    if b[1] == "Delhi":
        d += 1
    elif b[1] == "Mumbai":
        m += 1
    else:
        ch += 1

if d > m and d > ch:
    print("Delhi")
elif m > d and m > ch:
    print("Mumbai")
else:
    print("Chennai")
    