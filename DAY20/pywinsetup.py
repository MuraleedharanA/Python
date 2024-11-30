import win32api
import win32com.client
import win32gui

print("windows version :",win32api.GetVersion())
print("Computer Name  : ",win32api.GetComputerName())
print("System Metrics :",win32api.GetSystemMetrics())

#win32gui.MessageBox(0,"Hello","Message",1)

def custom_message():
    result = win32gui.MessageBox(0,'Do you like python ?',"Custom Message",1)
    if result==1:
        win32gui.MessageBox(0,str(result),"Output",1)

custom_message()