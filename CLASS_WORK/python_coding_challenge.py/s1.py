seats = {
1: "Booked",
2: "Available",
3: "Booked",
4: "Available",
5: "Booked",
6: "Booked",
7: "Available",
8: "Booked",
9: "Available",
10: "Booked"
}

# 1. Display available seats
print("Available seats:")
for i in seats:
    if seats[i] == "Available":
        print(i)

# 2. Count booked and available seats
booked = 0
available = 0

for i in seats:
    if seats[i] == "Booked":
        booked += 1
    else:
        available += 1

print("Booked seats =", booked)
print("Available seats =", available)

# 3. Reserve first available seat
for i in seats:
    if seats[i] == "Available":
        seats[i] = "Booked"
        print("Seat", i, "reserved")
        break

# 4. Cancel booking
num = int(input("Enter seat number to cancel: "))
if num in seats:
    seats[num] = "Available"
    print("Booking cancelled")
else:
    print("Invalid seat number")

# 5. Store in file
f = open("reservations.txt", "w")
for i in seats:
    f.write(str(i) + " : " + seats[i] + "\n")
f.close()

# 6. Occupancy percentage
total = len(seats)
booked = 0

for i in seats:
    if seats[i] == "Booked":
        booked += 1

percent = (booked / total) * 100
print("Occupancy =", percent, "%")
        

