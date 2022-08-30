import time
from datetime import datetime,date

now = datetime.now()
now2 = time.time()
print(now)
print(now2)


time1=2021-11-17
time2 = datetime.ctime(time1)
print(type(time2),time2)