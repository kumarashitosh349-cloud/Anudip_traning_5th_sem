temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

above_40 = []
pleasant = []

total = 0
count = 0

hot_city = ""
cool_city = ""
max_temp = 0
min_temp = 100

for city in temperature:
    temp = temperature[city]

    total = total + temp

    if temp > 40:
        above_40.append(city)

    if temp < 35:
        pleasant.append(city)

    if 35 <= temp <= 40:
        count = count + 1

    if temp > max_temp:
        max_temp = temp
        hot_city = city

    if temp < min_temp:
        min_temp = temp
        cool_city = city

avg = total / 10

print("Above 40:", above_40)
print("Hottest city:", hot_city)
print("Coolest city:", cool_city)
print("Average temperature:", avg)
print("Pleasant cities:", pleasant)
print("Count (35-40):", count)