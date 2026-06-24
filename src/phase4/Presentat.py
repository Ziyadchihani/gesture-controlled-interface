import pyautogui
import time


class PresentationController:

    def __init__(self):
        self.last_time = 0
        self.cooldown = 1.0  # seconds

    def _can_run(self):
        now = time.time()
        if now - self.last_time > self.cooldown:
            self.last_time = now
            return True
        return False

    def execute(self, gesture):

        if not self._can_run():
            return

        # NEXT SLIDE
        if gesture == "INDEX":
            pyautogui.press("right")
            print("NEXT SLIDE")

        # PREVIOUS SLIDE
        elif gesture == "PEACE":
            pyautogui.press("left")
            print("PREVIOUS SLIDE")

        # START PRESENTATION
        elif gesture == "OPEN_PALM":
            pyautogui.press("f5")
            print("START PRESENTATION")

        # EXIT PRESENTATION
        elif gesture == "FIST":
            pyautogui.press("esc")
            print("EXIT PRESENTATION")