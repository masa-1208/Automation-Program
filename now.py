from datetime import datetime

t = datetime.now()
fmt = t.strftime('%Y,%m,%d %H, %M %S')
print(fmt)