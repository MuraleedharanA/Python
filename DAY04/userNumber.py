def printUserDetails(name,number):
    '''Function to print Name of user N times'''
    for i in range(number):
        print("Name is :",name)

print("Enter your Name : ")
name=input()
print("Enter count to print : ")
number=int(input())
printUserDetails(name,number)