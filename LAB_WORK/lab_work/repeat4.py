while True:
    print("1. Area")
    print("2. Perimeter")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Area =", area)
    elif choice == "2":
        print("Perimeter =", perimeter)

    again = input("Do again? (Y/N): ")
    if again=="Y":
        choice = input("enter choice: ")
   

    if again == "N":
        break