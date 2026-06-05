transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0
deposits = []
withdrawals = []

deposit_count = 0
withdrawal_count = 0

largest_deposit = 0
largest_withdrawal = 0

for t in transactions:
    balance += t

    if t > 0:
        deposits.append(t)
        deposit_count += 1
        if t > largest_deposit:
            largest_deposit = t
    else:
        withdrawals.append(t)
        withdrawal_count += 1
        if t < largest_withdrawal:
            largest_withdrawal = t

print("Balance:", balance)
print("Total deposits:", deposit_count)
print("Total withdrawals:", withdrawal_count)
print("Largest deposit:", largest_deposit)
print("Largest withdrawal:", largest_withdrawal)
print("Deposits list:", deposits)
print("Withdrawals list:", withdrawals)