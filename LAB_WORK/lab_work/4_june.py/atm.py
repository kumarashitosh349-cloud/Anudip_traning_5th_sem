balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance =", balance)

    elif:
         choice == "2":
        amt = float(input("Enter money to deposit: "))
            balance = balance + amt
            print("Money added")

        else:
            if choice == "3":
                amt = float(input("Enter money to withdraw: "))
                
                if amt <= balance:
                    balance = balance - amt
                    print("Money withdrawn")
                else:
                    print("Not enough balance")

            else:
                if choice == "4":
                    print("Exit")
                    break
                else:
                    print("Wrong choice")

print("Final Balance =", balance)