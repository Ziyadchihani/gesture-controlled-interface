class GestureDetector:

    def fingers_up(self, landmarks):

        if not landmarks:
            return []

        fingers = []

        # Thumb (right-hand assumption)
        fingers.append(
            1 if landmarks[4][1] > landmarks[3][1] else 0
        )

        # Other fingers
        for tip in [8, 12, 16, 20]:
            fingers.append(
                1 if landmarks[tip][2] < landmarks[tip - 2][2] else 0
            )

        return fingers

    def recognize_gesture(self, fingers):

        fingers = tuple(fingers)

        gestures = {
            (0, 0, 0, 0, 0): "FIST",
            (1, 1, 1, 1, 1): "OPEN_PALM",
            (0, 1, 0, 0, 0): "INDEX",
            (0, 1, 1, 0, 0): "PEACE",
            (1, 0, 0, 0, 0): "THUMBS_UP"
        }

        return gestures.get(fingers, "UNKNOWN")