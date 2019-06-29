#!/usr/bin/env python 
#
# Working with PDF files 
#
import PyPDF2 

with open('Python_Scripting.pdf', 'rb') as pdf: 
  read_pdf = PyPDF2.PdfFileReader(pdf) 
  print 'Number of pages in pdf:', read_pdf.numPages
