def main():
	from PyPDF2 import PdfFileReader, PdfFileWriter
	import os

	pdf_document = "example2.pdf"
	pdf = PdfFileReader(pdf_document)

	# Output files for new PDFs
	output_filename = "output.pdf"
	pdf_writer= PdfFileWriter()

	numPages = pdf.getNumPages()
	print("> Input file has {} pages".format(numPages))



	if numPages % 2 !=0:
		numPages = numPages+1
		for page in range(int(numPages/2)):
			if page == 0:
				current_page = pdf.getPage(page)
				pdf_writer.addPage(current_page) 
				pdf_writer.addBlankPage()
			else:
				current_page = pdf.getPage(page)
				pdf_writer.addPage(current_page) 
				current_page = pdf.getPage(numPages-page-1)
				pdf_writer.addPage(current_page)
			
	else:
		for page in range(int(numPages/2)):
			current_page = pdf.getPage(page)
			pdf_writer.addPage(current_page) 
			current_page = pdf.getPage(numPages-page-1)
			pdf_writer.addPage(current_page)

	# Write the data to disk
	with open(output_filename, "wb") as out:
	     pdf_writer.write(out)
	     print("> created", output_filename)

if __name__== "__main__":
  main()



