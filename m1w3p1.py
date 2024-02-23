def sumTheNumber(num1, num2) :
    print("Sum =", num1 + num2)

def multiplyTheNumbers(num1, num2) :
    print("Product = ", num1 * num2)

def subtractTheNumbers(num1, num2) :
    print("Difference = ", num1 - num2)

def  divideTheNumbers(num1, num2): 
    print("Quotent = ", num1/num2)

while True :
    choice = input("TO PERFORM ADDITION type : add \nTO PERFORM SUBSTRACTION  type: subtract \nTO PERFORM MULTIPLICATION TYPE : multiply \nTO PERFORM DIV==ION type : divide \nTO CLOSE the program type : close :: ")
    if choice == "add" :
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        sumTheNumber(num1,num2)
    elif choice == "subtract" :
        pass
    elif choice == "multipy" :
        pass
    elif choice == "divide" :
        pass
    elif choice == "close" :
        break
    else : print("Try again.")