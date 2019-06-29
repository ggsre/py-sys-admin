#!/usr/bin/env python 
#
# Working with PDF files - Extracting Text 
#
import PyPDF2 

with open('Python_Scripting.pdf', 'rb') as pdf: 
  read_pdf = PyPDF2.PdfFileReader(pdf) 
  pdf_page = read_pdf.getPage(1) 
  pdf_content = pdf_page.extractText() 
  print pdf_content
