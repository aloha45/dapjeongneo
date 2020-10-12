import time

boop = time.ctime()

x = boop.split()

y = x[3]

z = y.split(':')

hours = int(z[0])
minutes = int(z[1])
seconds = int(z[2])

while True:
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
    if hours > 12:
        hours = hours - 12
    dtime = (str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
    print(dtime)