import openpyxl as excel

book = excel.Workbook()
sheet = book.active

for i in range(1,10):
    for j in range(1,10):
        cell = sheet.cell(row=i,column=j)
        cell.value = cell.coordinate

book.save("test_coordinate.xlsx")