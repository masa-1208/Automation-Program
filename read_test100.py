import openpyxl as excel

book = excel.load_workbook("test100.xlsx")
sheet = book.active

print(sheet["H2"].value)

cell = sheet.cell(row=111, column=7)
print(cell.value)