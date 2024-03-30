import openpyxl as excel

book = excel.Workbook()
sheet = book.active

sheet["A1"] = "hello 1"

sheet.cell(row=2, column=1, value="hello 2")

cell = sheet.cell(row=3, column=1)
cell.value = "hello 3"

book.save("cell_w.xlsx")