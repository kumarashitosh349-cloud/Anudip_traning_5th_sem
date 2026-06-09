present = 0
absent = 0

for i in range(1, 31):  
    status = input("Enter attendance  (P/A): ")

    if status == 'P':
        present += 1
    elif status == 'A':
        absent += 1
    else:
        print("Invalid input, try again")
        i -= 1 

        



print("Total Present:", present)
print("Total Absent:", absent)




      