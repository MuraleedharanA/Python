import win32com.client

def createExcel(filPath):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True

    workbook = workbook.Sheets(1)

    sheet = workbook.Sheets(1)
    sheet.Cells(1,1).Value = "Column1"
    sheet.Cells(2,1).Value = "Value"
    workbook.SaveAs(filPath)

    excel.Quit()

createExcel("sample.xlsx")
