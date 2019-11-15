import camelot
tables = camelot.read_pdf("bar.pdf")
#
table
#get shape of first table
tables[0]


#translate camelot object to pandas df
tables[0].df



for table in tables:
	print(table.df)


#output to csv -pandas
table_one = tables[0]
table_one.to_csv("foo.csv")


#output to excel
table_one.to_excel("foo.xlsx")

table_one.to_excel("foo.xlsx",index=False)



#Table with area

tables1 = camelot.read_pdf("bar.pdf", pages='32', area=[269.875, 120.75, 790.5, 561])
print (tabulate(tables1[0].df))

for i in range(30,35):
    print (i)
    tables = camelot.read_pdf("bar.pdf", pages='%d' %  i)
    try:
        print (tabulate(tables[0].df))
        print (tabulate(tables[1].df))
    except IndexError:
        print('NOK')











import PyPDF2
pdf_file = open('./tmp/pdf/Food Calories List.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(2)
page_content = page.extractText()
print (page_content.encode('utf-8'))







