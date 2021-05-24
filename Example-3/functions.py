from simple_device import SimpleDevice
from datetime import datetime

dayState = SimpleDevice()

day_time_list = []
night_time_list = []

class getInfo:

    def get_day_time_list(self, DAY_TIME_STARTED, NIGHT_TIME_STARTED):
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


    def get_state(self, day_time_list, night_time_list):
        now = datetime.now()
        current_hour = now.strftime("%H")

        for time_value in night_time_list:
            if current_hour == time_value:
                dayState.on_event('enter_night_state')

        for time_value in day_time_list:
            if current_hour == time_value:
                dayState.on_event('enter_day_state')