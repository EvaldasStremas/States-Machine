from datetime import datetime
import time, threading
from inputs import *
from functions import getInfo
from simple_device import SimpleDevice

getData = getInfo()
# dayState = SimpleDevice()

def main():
    time_list = getData.get_day_time_list(DAY_TIME_STARTED, NIGHT_TIME_STARTED)
    day_time_list = time_list[1]
    night_time_list = time_list[0]

    ticker = threading.Event()
    while not ticker.wait(CHECK_INTERVALS):
        getData.get_state(day_time_list, night_time_list)

if __name__ == "__main__":
    main()