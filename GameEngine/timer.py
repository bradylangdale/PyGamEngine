import time


def ms():
    return time.time() * 1000


class Timer:
    def __init__(self):
        self.start_time = ms()
        self.paused_at_time = 0
        self.paused = False

    @property
    def elapsed(self):
        if not self.paused:
            return ms() - self.start_time
        else:
            return self.paused_at_time

    def restart(self):
        self.start_time = ms()

    def set_time(self, x):
        """Note, must pass in negatives to add the value.
         Handy for punishing a player by subtracting the time on the clock.
          On the other hand, positive values will decrease the timer."""
        self.start_time += x

    def pause(self):
        if self.paused:
            return
        self.paused = True
        self.paused_at_time = ms() - self.start_time

    def resume(self):
        if not self.paused:
            return
        self.paused = False
        self.start_time = ms() - self.paused_at_time
