b = 10000

while True:
    c = int(input("1.Check 2.Deposit 3.Withdraw 4.Exit: "))

    if c == 1:
        print("Balance:", b)

    elif c == 2:
        b += int(input("Amount: "))

    elif c == 3:
        a = int(input("Amount: "))
        if a <= b:
            b -= a
        else:
            print("Low Balance")

    elif c == 4:
        break