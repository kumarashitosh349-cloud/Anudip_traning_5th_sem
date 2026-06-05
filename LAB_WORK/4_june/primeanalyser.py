n = int(input("enter a number: "))
count = 0


for i in range(1, n + 1):
    if n % i == 0:
        count += 1


if count == 2:
    print("Prime")
else:
    print("Not a prime")
    print("Factors:")
    for j in range(1, n + 1):
        if n % j == 0:
            print(j, end=" ")
    



     
           


