from pyPdf import PdfFileWriter,PdfFileReader
pdf=PdfFileReader(file('aa.pdf','rb'))
pagenum=pdf.numPages
pagelist=[[1,2],[3,4,5],[6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
for i in range(len(pagelist)):
	out=PdfFileWriter()
	for j in range(len(pagelist[i])):
		out.addPage(pdf.getPage(pagelist[i][j]-1))
		ous=file('set'+str(i+1)+'.pdf','wb')
		out.write(ous)
		ous.close()
