repeat = "Y"

while repeat == "Y":

    choice = input("Enter 1 for Area, 2 for Perimeter: ")

    if choice == "1":
        print("Area =", area)

    elif choice == "2":
        print("Perimeter =", perimeter)

    else:
        print("Wrong choice")

    repeat = input("Do you want to continue? (Y/N): ")

    if repeat == "Y":
        print("Continuing...\n")
    else:
        print("Stopping...")