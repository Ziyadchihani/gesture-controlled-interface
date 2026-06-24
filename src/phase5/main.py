import cv2

from hand import HandTracker
from swip import SwipeDetector
from Presentat import PresentationController
import time


def main():

    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    swipe = SwipeDetector()
    controller = PresentationController()

    last_action = None
    action_time = 0
    action_delay = 1.0   # IMPORTANT FIX

    while True:

        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)

        frame, landmarks = tracker.find_hands(frame)

        swipe_result = "NONE"

        if landmarks:

            x = landmarks[8][1]
            y = landmarks[8][2]

            swipe_result = swipe.update((x, y))

            now = time.time()

            # 🔥 KEY FIX: prevent repeat execution
            if swipe_result != "NONE":

                if swipe_result != last_action or (now - action_time > action_delay):

                    controller.execute(swipe_result)

                    last_action = swipe_result
                    action_time = now

        cv2.putText(
            frame,
            f"Swipe: {swipe_result}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        cv2.imshow("Final Swipe Controller", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()