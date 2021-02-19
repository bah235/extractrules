# importing required modules
import PyPDF2
import pikepdf
import tabula


with pikepdf.open('rules/event202.pdf') as pdf:
  num_pages = len(pdf.pages)
  pdf.save("decrypted.pdf")

# import tabula
# tabula.read_pdf("decrypted.pdf", stream=True)

import PyPDF2
pdfFileObj=open("decrypted.pdf", "rb")
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj=pdfReader.getPage(5)
print(pageObj.extractText())