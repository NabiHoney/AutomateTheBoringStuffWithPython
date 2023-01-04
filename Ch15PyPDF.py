import PyPDF2
pdfFileObj = open('#YourPDF', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))
pageObj = pdfReader.pages[1]
print(pageObj.extract_text())

#Updated to reflect changes in PyPDF2
