import pickle
import re
import xlrd

workbook = xlrd.open_workbook("IPTC-Subject-NewsCodes.xls")
worksheet = workbook.sheet_by_index(0)

numrows = worksheet.nrows 

ont = {}
list = []

i = 1
while i < numrows: 
    if worksheet.cell_value(i,2)!='':
        del list
        list = []
        name = worksheet.cell_value(i,7)
        name = re.sub(',','',name)
        ont[name] = list
    else:
        list.append(worksheet.cell_value(i,7))
    i += 1

#print ont

with open('onto.txt', 'wb') as handle:
    pickle.dump(ont, handle)

with open('onto.txt', 'rb') as handle:
    b = pickle.loads(handle.read())

workbook.close()
#print b

