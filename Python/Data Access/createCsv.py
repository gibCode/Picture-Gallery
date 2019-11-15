import csv


csvFile = open("../foo.csv", 'w+', newline='')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('value', 'product'))
    for i in range(10):
        writer.writerow( (i, i*i))
finally:
    csvFile.close()
