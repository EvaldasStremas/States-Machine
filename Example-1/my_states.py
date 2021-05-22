# my_states.py

from state import State

# Start of our states
class LockedState(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def on_event(self, event):
        if event == 'pin_entered':
            return UnlockedState()
        elif event == 'enter_sleep':
            return SleepState()

        return self

class UnlockedState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()
        elif event == 'enter_sleep':
            return SleepState()

        return self

class SleepState(State):
    """
    Sleep state
    """

    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()
        elif event == 'pin_entered':
            return UnlockedState()

        return self