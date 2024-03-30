from datetime import datetime
import math

sleep_t = datetime(2023, 1, 1, 22, 0, 0)
wakeup_t = datetime(2023, 1, 2, 8, 10, 0)

delta = wakeup_t - sleep_t
print(type(delta))
sec = delta.seconds
hours = sec / (60*60)
hours_integer = math.floor(hours)
minutes = round((hours - hours_integer)*60)

print('睡眠時間は'+str(hours_integer)+'時間'+str(minutes)+'分')