#Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    choice = input("Enter your choice [1-5] :\n1.Sum\n2.Sub\n3.Mul\n4.Div\n5.Quit\n")
    if choice in ['1','2','3','4','5']:
        if choice == '5':
            print("Ok byeeee!")
            break
      
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == '1':
            print(f"{num1}+{num2}=", add(num1, num2))

        elif choice == '2':
            print(f"{num1}-{num2}=", subtract(num1, num2))

        elif choice == '3':
            print(f"{num1}*{num2}= ", multiply(num1, num2))

        elif choice == '4':
            print(f"{num1}/{num2}=", divide(num1, num2))
    else:
        print("Not a valid choice")

