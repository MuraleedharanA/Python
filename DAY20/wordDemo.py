import win32com.client

def createWord(filePath):
    word = win32com.client.Dispatch(Word.Application)
    word.Visible = True
    doc = word.Documets.Add()

    selection = word.Selection
    selection.TypeText("Hi")
    selection.TypeParagraph()
    selection.TypeText("Hello")

    doc.SaveAs()

createWord("worddemo.docx")