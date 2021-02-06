from datetime import datetime
import time

while True:
    fname = '/shared/index.html'
    with open(fname, 'w') as f:
        now = datetime.now()
        f.write(now.strftime("%H:%M:%S on %A, %B the %dth, %Y"))
        time.sleep(3600)
