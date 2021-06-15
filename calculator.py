print("Advanced Calculator")
import math_operations
import comparison
import additional_operators
run=True
def exit_code():
    global run
    run=False
while run:
    print("Choose your options")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Modulo")
    print("6: Check for greater than")
    print("7: Check for less than")
    print("8: Check for equal to")
    print("9: Power")
    print("10: Pi")
    print("11: Square root")
    print("12: Squared")
    print("13: Cube root")
    print("14: Cubed")
    print("15: Exit")
    option=int(input(""))
    num1=float(input("Enter your first number "))
    num2=float(input("Enter your second number "))
    if option == 1:
        add=math_operations.add(num1,num2)
        print(add)
    elif option==2:
        sub=math_operations.sub(num1,num2)
        print(sub)
    elif option==3:
        multiply=math_operations.multiply(num1,num2)
        print(multiply)
    elif option==4:
        divide=math_operations.divide(num1,num2)
        print(divide)
    elif option==5:
        modulo=math_operations.mod(num1,num2)
        print(modulo)
    elif option==6:
        res=comparison.greater(num1,num2)
        print(res)
    elif option==7:
        res=comparison.less(num1,num2)
        print(res)
    elif option==8:
        res=comparison.equal(num1,num2)
    elif option==9:
        res=additional_operators.power(num1,num2)
        print(res)
    elif option==10:
        res=additional_operators.pi(num1,num2)
        print(res)
    elif option==11:
        res=additional_operators.square_root(num1,num2)
        print(res)
    elif option==12:
        res=additional_operators.squared(num1,num2)
        print(res)
    elif option==13:
        res=additional_operators.cube_root(num1,num2)
        print(res)
    elif option==14:
        res=additional_operators.cubed(num1,num2)
        print(res)
    elif option==15:
        exit_code()
    else:
        print("Unknown option")
        exit_code()
