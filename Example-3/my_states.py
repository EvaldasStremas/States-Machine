# my_states.py

from state import State

class DayState(State):

    def on_event(self, event):
        if event == 'enter_night_state':
            return NightState()

        return self

class NightState(State):

    def on_event(self, event):
        if event == 'enter_day_state':
            return DayState()

        return self