"""
1.create a dict of sample data
2.menu driven loop to  add data into the dic based on user input
3. one of the option shld be print the daTAframe
"""
import pandas as pd

def addData(dict_Sample):
    key=input("Enter Column Name :")
    val=input("Enter Corresponding values :")
    dict_sample[key]=val.split(" ")
    return dict_sample

def printData(dict_Sample):
    df=pd.DataFrame(dict_sample)
    print(df)

dict_sample={}
option=-1
while(option!=3):
    print("********MENU***********\n1. Add Data\n2. PrintData\n3. Exit")
    option=int(input("Enter your option : "))
    if(option==1):
        addData(dict_sample)
    elif(option==2):
        printData(dict_sample)


