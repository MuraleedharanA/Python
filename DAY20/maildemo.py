import win32com.client

def sendEmail(subj, body, to_email):
    outlook = win32com.client.Dispatch("Outlook.Application")


    mail = outlook.CreateItem(0)
    mail.Subject = subj
    mail.Body = body
    mail.To = to_email
    mail.send()

sendEmail("Request","Accepted your request","251210@ust.com")
