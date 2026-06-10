"""Prime NO."""

 = int(input("enter a number: "))
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




    

"""Armstrong"""
um = int(input("Enter number: "))

sum = 0
n = num

while n > 0:
    digit = n % 10
    sum = sum + digit**3
    n = n // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")





    """strong number"""
mport math

num = int(input("Enter a number: "))
original = num
sum_factorial = 0

# Calculate sum of factorials of digits
while num > 0:
    digit = num % 10
    sum_factorial += math.factorial(digit)
    num //= 10

# Check if it's a strong number
if sum_factorial == original:
    print(f"{original} is a Strong Number")
else:
    print(f"{original} is NOT a Strong Number")





    """number guessing"""
    while True:
    guess = int(input("Enter your guess (1-50): "))
    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess")
        print("Total attempts:", attempts)
        break




    """electricity bill"""
    units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
    category = "Low Consumption"
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
    category = "Medium Consumption"
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    category = "High Consumption"

print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Category:", category)




"""pyramid"""
n = int(input())

# Normal pattern
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

# Reverse pattern
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()










    """employee payroll"""

    name = input("Enter name: ")
basic = int(input("Enter salary: "))

hra = basic * 0.2
da = basic * 0.1
pf = basic * 0.12

gross = basic + hra + da
net = gross - pf

if net > 50000:
    grade = "Senior Grade"
elif net > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

print("Gross Salary:", gross)
print("Net Salary:", net)
print("Grade:", grade)




"""palindrome"""
n = input()

rev = n[::-1]

print("Reverse:", rev)

if n == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome")



   """atm"""
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





"""student"""
tal = 0
fail_count = 0

for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    total = total + m
    
    if m < 40:
        fail_count = fail_count + 1

# Calculate percentage
percentage = total / 5

# Decide grade using only if-else
if percentage >= 90:
    grade = "A+"
else:
    if percentage >= 75:
        grade = "A"
    else:
        if percentage >= 60:
            grade = "B"
        else:
            if percentage >= 40:
                grade = "C"
            else:
                grade = "Fail"

# Display result
print("\n--- Result ---")
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Number of subjects failed =", fail_count)