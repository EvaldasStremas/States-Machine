from simple_device import SimpleDevice
from datetime import datetime
import time, threading
from inputs import *

day_time_list = []
night_time_list = []

dayState = SimpleDevice()

class getInfo:

    def get_day_time_list(DAY_TIME_STARTED, NIGHT_TIME_STARTED):
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

        return night_time_list, day_time_list


    def get_state(day_time_list, night_time_list):
        now = datetime.now()
        current_hour = now.strftime("%H")

        for time_value in night_time_list:
            if current_hour == time_value:
                dayState.on_event('enter_night_state')

        for time_value in day_time_list:
            if current_hour == time_value:
                dayState.on_event('enter_day_state')


    # def start_timer():
    #     getInfo.get_state(day_time_list, night_time_list)
    #     threading.Timer(2, getInfo.start_timer).start()

time_list = getInfo.get_day_time_list(DAY_TIME_STARTED, NIGHT_TIME_STARTED)
day_time_list = time_list[1]
night_time_list = time_list[0]

# getInfo.start_timer()

ticker = threading.Event()
while not ticker.wait(CHECK_INTERVALS):
    getInfo.get_state(day_time_list, night_time_list)
    print(dayState.state)