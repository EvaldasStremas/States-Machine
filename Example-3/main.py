from simple_device import SimpleDevice
from datetime import datetime
import time

time_list = []

for time in range(1,24):
    time_list.append(time)

dayState = SimpleDevice()

for current_time in time_list:

    if current_time == 9:
        dayState.on_event('enter_day_state')
    elif current_time == 20:
        dayState.on_event('enter_night_state')
    else:
        print('Now is',dayState.state, 'and hours', current_time)