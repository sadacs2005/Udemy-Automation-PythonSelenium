import xlrd

# Create an object of workbook
objWorkBook = xlrd.open_workbook("C:/Users/Sadashiva Ashok/PycharmProjects/AutomationProjectDCI/ReadExcel.xlsx")

# Get the number of sheets in the excel
print("No of sheets in the excel is "+str(objWorkBook.nsheets))

# Get into each sheet level
objWorkSheet = objWorkBook.sheet_by_name("Sheet1")
no_of_rows = objWorkSheet.nrows
no_of_columns = objWorkSheet.ncols

# Get the data from the cell
# objCell = objWorkSheet.cell(5, 0)
# print("The value in the cell is "+objCell.value)

# Read all the values in the cell
for i in range(1, no_of_rows):
    for j in range(0, no_of_columns):
        objCell = objWorkSheet.cell(i, j)
        print(objCell.value)


