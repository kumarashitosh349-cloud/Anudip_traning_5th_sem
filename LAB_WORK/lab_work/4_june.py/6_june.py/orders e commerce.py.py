orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# > 1000
for i in orders:
    if i[1] > 1000:
        print(i)

# most expensive
price = 0
name = ""
for i in orders:
    if i[1] > price:
        price = i[1]
        name = i[0]
print(name, price)

# total
total = 0
for i in orders:
    total += i[1]
print(total)

# < 1000 count
count = 0
for i in orders:
    if i[1] < 1000:
        count += 1
print(count)




    
   


     
