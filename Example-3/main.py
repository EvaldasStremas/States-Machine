from simple_device import SimpleDevice
from datetime import datetime
import time

DAY_TIME_STARTED = 8
NIGHT_TIME_STARTED = 20
CHECK_INTERVALS = 2

day_time_list = []
night_time_list = []

for day_time in range(DAY_TIME_STARTED, NIGHT_TIME_STARTED):
    if len(str(day_time)) == 1:
        day_time_list.append('0' + str(day_time))
    else:
        day_time_list.append(str(day_time))

for night_time in range(NIGHT_TIME_STARTED, 24):
    if len(str(night_time)) == 1:
        night_time_list.append('0' + str(night_time))
    else:
        night_time_list.append(str(night_time))

for night_time in range(0, DAY_TIME_STARTED):
    if len(str(night_time)) == 1:
        night_time_list.append('0' + str(night_time))
    else:
        night_time_list.append(str(night_time))

dayState = SimpleDevice()

while True:

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_hour = now.strftime("%H")

    print("Current Time =", current_time)

    for time_value in night_time_list:
        if current_hour == time_value:
            dayState.on_event('enter_night_state')

    for time_value in day_time_list:
        if current_hour == time_value:
            dayState.on_event('enter_day_state')
    
    time.sleep(CHECK_INTERVALS)