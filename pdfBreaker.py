#! python3

# pdfBreaker uses a dictionary file to brute-force attack encrypted PDFs, we will use dictionary.txt and encrypted.pdf

import os, PyPDF2

#Load dictionary file and pdf we will be attacking
print('Loading dictionary from dictionary.txt...')
dictionaryFile = open('dictionary.txt')
dictionaryList = dictionaryFile.readlines()

print('Loading target PDF file from encrypted.pdf...')
pdfFile = open('encrypted.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(pdfFile)
print(f"The PDF file is encrypted: {pdf.isEncrypted}")

#todo try each string as a password for a decrypt call to the pdf, if we find the password break the loop and print the password
for word in dictionaryList:
    print(f"Trying upper and lowercase versions of: {word}.")
    if pdf.decrypt(str.upper(word)) == '1' or pdf.decrypt(str.lower(word)) == '1':
        print(f"The password is {word}.")
        break
