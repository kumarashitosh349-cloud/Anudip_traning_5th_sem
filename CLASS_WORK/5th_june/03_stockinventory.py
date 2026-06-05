stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = []
restock = []
available_count = 0
high_stock = []

for s in stock:
    if s == 0:
        out_of_stock.append(s)

    if s < 10:
        restock.append(s)

    if s > 0:
        available_count += 1

    if s >= 15:
        high_stock.append(s)

print("Out of stock products:", out_of_stock)
print("Need restocking products:", restock)
print("Available products count:", available_count)
print("Products with stock >= 15:", high_stock)