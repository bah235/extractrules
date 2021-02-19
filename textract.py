# importing required modules
import PyPDF2
import pikepdf
import tabula


# creating a pdf file object 
pdfFileObj = open('rules/event202.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
print(pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() 



import pikepdf
with pikepdf.open("encrypted.pdf") as pdf:
  num_pages = len(pdf.pages)
  del pdf.pages[-1]
  pdf.save("decrypted.pdf")

import tabula
tabula.read_pdf("decrypted.pdf", stream=True)

import PyPDF2
pdfFileObj=open("decrypted.pdf", "rb")
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj=pdfReader.getPage(0)
pageObj.extractText()