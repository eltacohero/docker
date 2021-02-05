from datetime import datetime
import time

while True:
    now = datetime.now()
    print(now.strftime("%H:%M:%S on %A, %B the %dth, %Y"))
    time.sleep(3600)
