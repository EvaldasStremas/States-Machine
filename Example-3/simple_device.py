# simple_device.py

from my_states import DayState

class SimpleDevice(object):

    def __init__(self):
        # Start with a default state.
        self.state = DayState()

    def on_event(self, event):
        self.state = self.state.on_event(event)