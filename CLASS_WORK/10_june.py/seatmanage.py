seats = [
"Booked", "Available", "Booked", "Booked",
"Available", "Available", "Booked", "Available",
"Booked", "Booked", "Available", "Booked"]

def count_seats(seats):
    booked = 0
    available = 0

    for seat in seats:
        if seat == "Booked":
            booked = booked + 1
        else:
            available = available + 1

    print("Booked seats =", booked)
    print("Available seats =", available)





def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            print("First available seat is:", i + 1)
            return i + 1
    print("No seat available")
    return None


def occupancy_percentage(seats):
    booked = 0

    for seat in seats:
        if seat == "Booked":
            booked = booked + 1

    total = len(seats)
    percent = (booked / total) * 100

    print("Occupancy percentage =", percent)


def display_available_seats(seats):
    print("Available seats are:")

    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1)


count_seats(seats)
first_available(seats)
occupancy_percentage(seats)
display_available_seats(seats)               





