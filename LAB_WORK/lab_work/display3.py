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

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter your choice: ")

            if op == "1":
                print("Area =", geometry.circle_area(radius))

            elif op == "2":
                print("Perimeter =", geometry.circle_perimeter(radius))

            elif op == "3":
                break

            else:
                print("Invalid choice!")

    elif choice == "2":
        print("You selected Square")
        side = float(input("Enter side: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter your choice: ")

            if op == "1":
                print("Area =", geometry.square_area(side))

            elif op == "2":
                print("Perimeter =", geometry.square_perimeter(side))

            elif op == "3":
                break

            else:
                print("Invalid choice!")

    elif choice == "3":
        print("You selected Rectangle")
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter your choice: ")

            if op == "1":
                print("Area =", geometry.rectangle_area(length, breadth))

            elif op == "2":
                print("Perimeter =", geometry.rectangle_perimeter(length, breadth))

            elif op == "3":
                break

            else:
                print("Invalid choice!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")