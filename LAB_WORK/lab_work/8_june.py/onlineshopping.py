sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

more_than_20 = [p for p in sales if sales[p] > 20]

best = max(sales, key=sales.get)
least = min(sales, key=sales.get)

total = sum(sales.values())

promotion = [p for p in sales if sales[p] < 15]

between_10_30 = sum(1 for v in sales.values() if 10 <= v <= 30)

print("More than 20:", more_than_20)
print("Best selling:", best)
print("Least selling:", least)
print("Total sold:", total)
print("Need promotion:", promotion)
print("Count (10-30):", between_10_30)
