import os
import datetime
import time

while True:
    os.system("cls")
    dt = datetime.datetime.now()
    print(f"\x1b[1;33m{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}")
    time.sleep(1)

