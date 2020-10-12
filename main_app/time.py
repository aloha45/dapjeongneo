import time
import datetime

boop = time.ctime()

x = boop.split()

y = x[3]

z = y.split(':')

hours = int(z[0])
minutes = int(z[1])
seconds = int(z[2])

dtime = 0

on = True

def dclock():
    # global seconds, minutes, hours
    global dtime
    x = boop.split()
    y = x[3]
    z = y.split(':')
    hours = int(z[0])
    minutes = int(z[1])
    seconds = int(z[2])
    while True:
        seconds = seconds + 1
        time.sleep(1)
        # dclock()
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
        # return (dtime)

dclock()

# def dclock2():
#     current_date = str(datetime.datetime.today())
#     current_time = current_date.split()[1]
#     basic_time = (current_time.split(':'))
#     hours = basic_time[0]
#     minutes = basic_time[1]
#     seconds = basic_time[2]
#     dtime = (str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
#     print(dtime)
#     # time.sleep(1)
#     # dclock2()

# dclock2()