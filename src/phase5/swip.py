import time
import math


class SwipeDetector:

    def __init__(self):

        self.start_pos = None
        self.start_time = None

        self.swipe = "NONE"

        self.cooldown = 0.8
        self.locked = False
        self.lock_time = 0

        self.time_window = 0.5   # IMPORTANT FIX
        self.min_distance = 80

    def update(self, position):

        if position is None:
            return self._output()

        x, y = position
        now = time.time()

        # ignore during cooldown
        if self.locked:
            return self._output()

        # start tracking
        if self.start_pos is None:
            self.start_pos = (x, y)
            self.start_time = now
            return "NONE"

        # check time window
        dt = now - self.start_time

        dx = x - self.start_pos[0]
        dy = y - self.start_pos[1]

        # still collecting movement
        if dt < self.time_window:
            return "NONE"

        distance = math.sqrt(dx * dx + dy * dy)

        # not enough movement → reset
        if distance < self.min_distance:
            self._reset()
            return "NONE"

        # detect direction ONCE
        if abs(dx) > abs(dy):

            if dx > 0:
                self._trigger("SWIPE_RIGHT")
            else:
                self._trigger("SWIPE_LEFT")

        else:

            if dy > 0:
                self._trigger("SWIPE_DOWN")
            else:
                self._trigger("SWIPE_UP")

        self._reset()
        return self._output()

    def _trigger(self, swipe):

        self.swipe = swipe
        self.locked = True
        self.lock_time = time.time()

    def _reset(self):

        self.start_pos = None
        self.start_time = None

    def _output(self):

        if self.locked and time.time() - self.lock_time > self.cooldown:
            self.locked = False

        if self.locked:
            return self.swipe

        return "NONE"