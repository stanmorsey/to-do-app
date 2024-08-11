def main_bar ():
    print(":::::Welcome! to our CLI CALCULATOR:::::")
    print("""
            1. Addition (+)
            2. Subtraction (-)
            3. Multiplication (x)
            4. Division (/) """)
    while True:
        try:
            choice  = int(input("Choose your operation (1-4)"))
            if choice in [1,2,3,4]:
                return choice
        except ValueError:
            print("Please only use integers to refer to the operation")
                
def add_value(x, y):
    return x + y

def subtract_value(x, y):
    return x - y

def multiply_value(x, y):
    return x * y

def divide_value(x, y):
    if y == 0:
        print ("Kindly input a valid number above 0")
    else:
        return x /y
    
def operation():
    x = float(input("Enter the first vallue: "))
    y = float(input("Enter second value: "))

    choice = main_bar()

    if choice == 1:
        print (f"\n The sum of {x} and {y} = {x + y}\n")
    elif choice ==2:
        print (f"\n The difference between {x} and {y} = {x - y}\n")
    elif choice ==3:
        print (f"\nThe product of {x} and {y} = {x * y}\n")
    elif choice ==4:
        print(f"\nThe division of {x} and {y} = {x /y}\n")
    else:
        print("\nYour selectiion is not valid\n")

def main():
    operation()

if __name__ == "__main__":
    main()
    