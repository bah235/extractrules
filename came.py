# importing required modules
import camelot
import pikepdf
import tabula
import pandas as pd


PDF_Name = 'event202.pdf'

def decrypt_pdf(filename):
    openpath = 'rules/encrypted/'
    savepath = 'rules/decrypted/'

    with pikepdf.open(openpath + filename) as pdf:
        num_pages = len(pdf.pages)
        pdf.save(savepath + filename)

decrypt_pdf(PDF_Name)


name_table = camelot.read_pdf("decrypted.pdf", pages = '1-end')
print(name_table)



# #To get all the tables of the pdf you need to use this code.
for table in name_table:
    print(table.df.replace('\n', ' ', regex=True))