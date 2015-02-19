import csv
# writes results to csv
def CsvWriteHeader(path, fieldNames):
    with open(path, 'aw') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(fieldNames)

def CsvWriterItems(pathItem,nodeCateName,itemDetails):
    print "writing to csv file with defined path {}......".format(pathItem)
    with open(pathItem, 'aw') as csvfile:
        itemWriter = csv.writer(csvfile, delimiter=',')
        itemDetails4write = [unicode(x).encode('utf-8') for x in itemDetails]
        itemWriter.writerow([nodeCateName]+itemDetails4write)
        
def CsvWriterRel(pathRel, superCateName, subCateName):
    print "writing to csv file with defined path {}......".format(pathRel)
    with open(pathRel, 'aw') as csvfile:
        relWriter = csv.writer(csvfile, delimiter=',')
        rel4write = [unicode(x).encode('utf-8') for x in [superCateName, subCateName]]
        relWriter.writerow(rel4write)
        