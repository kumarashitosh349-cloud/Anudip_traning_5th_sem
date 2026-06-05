seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0
available_seats = []
first_available = -1

for i in range(len(seats)):
    if seats[i] == 1:
        booked += 1
    else:
        available += 1
        available_seats.append(i)

        if first_available == -1:
            first_available = i

occupancy = booked / len(seats)

print("Booked seats:", booked)
print("Available seats:", available)
print("First available seat:", first_available)
print("Available seat numbers:", available_seats)

if occupancy > 0.7:
    print("Bus is more than 70% occupied")
else:
    print("Bus is 70% or less occupied")