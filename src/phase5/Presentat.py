import pyautogui


class PresentationController:

    def __init__(self):
        pass

    def execute(self, swipe):

        if swipe == "SWIPE_RIGHT":
            pyautogui.press("right")
            print("NEXT SLIDE")

        elif swipe == "SWIPE_LEFT":
            pyautogui.press("left")
            print("PREVIOUS SLIDE")

        elif swipe == "SWIPE_UP":
            pyautogui.press("f5")
            print("START PRESENTATION")

        elif swipe == "SWIPE_DOWN":
            pyautogui.press("esc")
            print("EXIT PRESENTATION")