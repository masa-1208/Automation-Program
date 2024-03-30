from datetime import datetime

conduct_date = datetime(2025, 4, 13)

now = datetime.now()

delta = conduct_date - now
print('あと'+str(delta.days+1)+'日')