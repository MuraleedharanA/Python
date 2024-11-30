import win32com.client

def getInbox(namespace):
    inbox = namespace.GetDefaultFolder(6) #6 = inbox
    messages = inbox.Items
    print(f"Total message :{len(inbox.Items)}")

    for i in range(min(5, len(messages))):
        message = messages[i]
        print(f"Subject :{message.Subject}")

namespace = outlook.GetNamespace("MAPI")
getInbox(namespace)