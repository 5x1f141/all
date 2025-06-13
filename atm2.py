balance = 10000

def show(balance):

    print("Your balance is : ",balance)

def deposit(balance,amount):

    balance+=amount
    return balance

def withdraw(balance,amount):

    if amount>balance:
        print("Not anough money!!")
        return balance
    else :
        balance -= amount
        return balance
while True :
    print ("\n--- Welcome To The ATM!!! ---")
    print("1) Show balance")
    print("2) Deposit money")
    print("3) Withdraw money")
    print("4) Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        show(balance)
    elif choice==2:
        amount=int(input("Enter amount to deposit :"))
        balance = deposit(balance,amount)
        print(balance)
    elif choice==3:
        amount=int(input("Enter amount to withdraw : "))
        balance = withdraw(balance,amount)
        print(balance)
    elif choice == 4:
        print("Goodbye!!")
        break
    else :
        print("Invaild choice! Please try again.")
