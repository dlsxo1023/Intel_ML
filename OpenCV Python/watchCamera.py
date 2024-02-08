import cv2
import numpy as np
import math
import time

def draw_clock(frame, center, radius, time_now, camera_frame, alpha=0.5):
    # Draw clock face
    cv2.circle(frame, center, radius, (255, 255, 255), -1)

    # Draw hour markers
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(1, 13):
        angle = math.radians(i * 30)
        x = int(center[0] + 0.8 * radius * math.sin(angle) - 10)
        y = int(center[1] - 0.8 * radius * math.cos(angle) + 5)
        cv2.putText(frame, str(i), (x, y), font, 0.7, (0, 0, 0), 2, cv2.LINE_AA)

    # Draw clock hands
    draw_hand(frame, center, radius * 0.6, math.radians(time_now.tm_hour * 30 + time_now.tm_min * 0.5 - 90), 8, (0, 0, 255))
    draw_hand(frame, center, radius * 0.8, math.radians(time_now.tm_min * 6 - 90), 4, (255, 0, 0))
    draw_hand(frame, center, radius * 0.9, math.radians(time_now.tm_sec * 6 - 90), 2, (0, 0, 0))

    # Resize and blend camera frame with transparency
    camera_frame_resized = cv2.resize(camera_frame, (2 * radius, 2 * radius))
    frame_resize=cv2.resize(frame, (2 * radius, 2 * radius))
    blended_frame = cv2.addWeighted(frame_resize, 1 - alpha, camera_frame_resized, alpha, 0)
    frame[center[1] - radius: center[1] + radius, center[0] - radius: center[0] + radius] = blended_frame

def draw_hand(frame, center, length, angle, thickness, color):
    x2 = int(center[0] + length * math.cos(angle))
    y2 = int(center[1] + length * math.sin(angle))
    cv2.line(frame, center, (x2, y2), color, thickness)

def main():
    window_size = 500
    center = (int(window_size / 2), int(window_size / 2))
    radius = int(window_size / 2) - 20

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    clock_frame = np.zeros((window_size, window_size, 3), dtype=np.uint8)

    while True:
        ret, camera_frame = cap.read()
        if not ret:
            break

        current_time = time.localtime()

        draw_clock(clock_frame, center, radius, current_time, camera_frame, alpha=0.7)

        cv2.imshow("Analog Clock with Transparent Camera", clock_frame)

        key = cv2.waitKey(100)

        if key == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

