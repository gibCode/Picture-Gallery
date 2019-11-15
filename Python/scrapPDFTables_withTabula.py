from tabula import read_pdf
from tabulate import tabulate


tbl = read_pdf("./temp/Tables.pdf")


# remove NaN columns

tbl = df.dropna(axis='columns')


tbl = read_pdf("./temp/Tables.pdf", pages=3)

# JSON format
tbl = read_pdf("./temp/Tables.pdf", pages=3, output_format="json")

tbl = read_pdf("./temp/Tables.pdf", pages='all', multiple_tables=True)

# Adjust area
tbl = read_pdf("./temp/Tables.pdf", encoding = 'ISO-8859-1',
         stream=True, area = [269.875, 12.75, 790.5, 961], pages = 4, guess = False,  pandas_options={'header':None})

tbl = read_pdf("./temp/Tables.pdf", encoding = 'ISO-8859-1',
         stream=True, guess = False)



tbl = read_pdf("./temp/Tables.pdf", encoding = 'ISO-8859-1',
         stream=True, area=[269.875, 12.75, 790.5, 961], guess = False)

