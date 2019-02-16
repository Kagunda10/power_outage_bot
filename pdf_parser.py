import PyPDF2
pdf_file_obj = open("Interruptions.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

page_obj = pdf_reader.getPage(0)
with open("tst.txt", "w") as  txt:
	txt.write(page_obj.extractText())