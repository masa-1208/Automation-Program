import openpyxl as excel
import datetime

book = excel.Workbook()
sheet = book.active

this_year = datetime.date.today().year

for i in range(81):
    age = i
    birth_year = this_year - age
    age_cell = sheet.cell(i+1, 1)
    age_cell.value = 'age:' + str(age)
    year_cell = sheet.cell(i+1, 2)
    year_cell.value = 'birth year:' + str(birth_year)

book.save("agelist.xlsx")