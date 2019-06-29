#!/usr/bin/env python 
#
# Working with PDF files - Rotating PDF
#
import PyPDF2 

with open('Python_Scripting.pdf', 'rb') as pdf: 
  rd_pdf = PyPDF2.PdfFileReader(pdf) 
  wr_pdf = PyPDF2.PdfFileWriter() 
  for pg_num in range(rd_pdf.numPages):
    pdf_page = rd_pdf.getPage(pg_num) 
    pdf_page.rotateClockwise(90)
    wr_pdf.addPage(pdf_page)

  with open('rotated.pdf', 'wb') as pdf_out:
    wr_pdf.write(pdf_out)

print 'PDF successfully rotated'
