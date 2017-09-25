import xlrd

filename = r'E:\123.xlsx'

data = xlrd.open_workbook(filename)

sheetname = data.sheet_names()

sheet = data.sheet_by_index(0) 

rows = sheet.nrows

cols = sheet.ncols

for row in range(rows):

   value = sheet.row_values(row)

   print(value)