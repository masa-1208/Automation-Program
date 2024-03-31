import openpyxl as excel
import datetime

book = excel.Workbook()
sheet = book.active

# first year to display
base_year = datetime.date.today().year - 10

for i in range(20):
    year = base_year + i
    s1 = year - 7
    s2 = year - 6
    sf = "{}~{}".format(s1, s2)

    sheet.cell(i+1, 1, value=year)
    sheet.cell(i+1, 2, value=sf)

book.save("enroll_year.xlsx")