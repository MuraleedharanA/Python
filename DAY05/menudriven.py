def operation(operand):
    a=(int(input("Enter Number a :")))
    b=(int(input("Enter Number b :")))
    if(operand=='+'):
        return a+b
    elif(operand=='-'):
        return a-b
    elif(operand=='*'):
        return a*b
        

option=0
while(option!=4):
    print("\n\n***********Menu*****************")
    print("1. Add Numbers\n2. Subtract Numbers\n3. Multiply Numbers \n4. Exit")
    print("Please enter your Option : ")
    option=int(input())
    if(option==1):
        print("Result :",operation("+"))
    elif(option==2):
        print("Result :",operation("-"))

    elif(option==3):
        print("Result :",operation("*"))
