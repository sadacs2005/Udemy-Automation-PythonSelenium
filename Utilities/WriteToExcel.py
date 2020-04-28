import xlwt

# Create an object of workbook
objWorkBook = xlwt.Workbook()
# Create an sheet
objWorkSheet = objWorkBook.add_sheet("SheetTest")
objWorkSheet.write(0, 0, "Data1")
objWorkSheet.write(0, 1, "Data2")
# Save the sheet
objWorkBook.save(".././WriteExcel.xls")