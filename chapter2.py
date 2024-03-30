import openpyxl as excel

book = excel.Workbook()

sheet = book.active

for i in range(1,10):
    for j in range(1,10):
        sheet.cell(row=i, column=j, value=i*j)

book.save("9times9.xlsx")