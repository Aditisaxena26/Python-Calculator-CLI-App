#calculator.py
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return x/y
    
def main():
    while True:
        print("Welcome to the Calculator CLI app!")
        print("Please select an operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        print("Please enter the choice :")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4','5']:
            if choice == '5':
                user_exit= input("Type 'QUIT' to exit the app: "
                "")
                if user_exit.upper() == 'QUIT':
                    print("Exiting the app.")
                    print("Thank you for using the Calculator CLI app!")
                    print("Goodbye!")
                    break
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if choice == '1':
                print("The result is: ",add(x, y))
            elif choice == '2':
                print("The result is: ",sub(x, y))
            elif choice == '3':
                print("The result is: ",mul(x, y))
            elif choice == '4':
                try:
                    print("The result is: ",div(x, y))
                except ValueError as e:
                    print(e)
        else:
            print("Invalid choice. Please try again.")
main()


