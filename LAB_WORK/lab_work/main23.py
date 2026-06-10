import geometry

while True:
    print("\n--- Select a Figure ---")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You selected Circle")
        radius = float(input("Enter radius: "))

    elif choice == "2":
        print("You selected Square")
        side = float(input("Enter side: "))

    elif choice == "3":
        print("You selected Rectangle")
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")
        