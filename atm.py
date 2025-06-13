balance = 1000

while True:
    print("\nWelcome to the ATM !!")
    print("1-) Show balance")
    print("2-) Deposit money")
    print("3-) Withdraw money")
    print("4-) Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        x = int(input("How much? : "))
        balance += x
        print("Your new balance is:", balance)

    elif choice == 3:
        y = int(input("How much? : "))
        if y > balance:
            print("Not enough money!!")
        else:
            balance -= y
            print("New balance:", balance)

    elif choice == 4:
        print("Have a nice day!!")
        break

    else:
        print("Invalid choice. Try again.")
