def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return("Error : cannot divide by zero!")
    return x/y

def menu():
    print("Mini calculator!")
    print("1) Add")
    print("2) subtract")
    print("3) multiply")
    print("4) divide")
    print("5) Exit")

while True:
    menu()
    choice=int(input("Enter choice (1-5) : "))
    if choice == 5:
        print("Goodbye!!")
        break

    num1=float(input("Enter number 1 : "))
    num2=float(input("Enter number 2 : "))
    if choice == 1:
        result = add(num1,num2)
        print("Result : ",result)
    elif choice == 2:
        result = subtract(num1,num2)
        print("Result : ",result)
    elif choice == 3:
        result = multiply(num1,num2)
        print("Result : ",result)
    elif choice == 4:
        result= divide(num1,num2)
        print("Result : ",result)
    else :
        print("Invaild Choice! Please try again")
