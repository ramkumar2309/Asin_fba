import sys
import xlrd
wb = xlrd.open_workbook('/Users/karuppig/Desktop/fetchAsin.xlsx')
sheet = wb.sheet_by_name('NAGamma')
pound_val=sheet.cell_value(0,1)
for i in range(sheet.nrows):
   data=(sheet.cell_value(i,0))
   a=Asin(asin=data,product=pound_val)
   a.save()

   Asin.objects.all()