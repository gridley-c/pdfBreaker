#! python3

# pdfBreaker uses a dictionary file to brute-force attack encrypted PDFs, we will use dictionary.txt and encrypted.pdf

import os, PyPDF2

#Load dictionary file and pdf we will be attacking
print('Loading dictionary from dictionary.txt...')
with open('dictionary.txt') as f:
    dictionaryList = [line.rstrip() for line in f]

print('Loading target PDF file from encrypted.pdf...')
pdfFile = open('encrypted.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(pdfFile)
print(f"The PDF file is encrypted: {pdf.isEncrypted}")

#todo try each string as a password for a decrypt call to the pdf, if we find the password break the loop and print the password
for word in dictionaryList:
    print(f"Trying upper and lowercase versions: \"{str.upper(word)}\" \"{str.lower(word)}\"")

    if pdf.decrypt(word.lower()):
        print("######################################")
        print(f"The password is {word.lower()}.")  
        print("######################################")
        break
    elif pdf.decrypt(word.upper()):
        print("######################################")
        print(f"The password is {word.upper()}.")
        print("######################################")
        break

pdfFile.close()
f.close()
