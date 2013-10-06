from pyPdf import PdfFileWriter,PdfFileReader
import os
os.chdir('/Users/a/Desktop/temp1')
out=PdfFileWriter()
for i in range(7):
	pdf=PdfFileReader(file(str(i+1)+'.pdf','rb'))
	pagenum=pdf.numPages
	print pagenum
	for k in range(pagenum):
		out.addPage(pdf.getPage(k))
ous=file('set.pdf','wb')
out.write(ous)
ous.close()
