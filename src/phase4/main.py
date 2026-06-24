import cv2

from hand import HandTracker
from generate import GestureDetector
from Presentat import PresentationController


def main():

    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    detector = GestureDetector()
    controller = PresentationController()

    while True:

        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)

        frame, landmarks = tracker.find_hands(frame)

        if landmarks:

            # Step 1: fingers
            fingers = detector.fingers_up(landmarks)

            # Step 2: gesture
            gesture = detector.recognize_gesture(fingers)

            # Step 3: control computer
            controller.execute(gesture)

            # UI display
            cv2.putText(
                frame,
                f"Gesture: {gesture}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Fingers: {fingers}",
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

        cv2.imshow("Phase 4 - Presentation Controller", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()