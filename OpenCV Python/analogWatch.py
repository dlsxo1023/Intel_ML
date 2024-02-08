import cv2
import numpy as np
import math
import time

def draw_clock(frame, center, radius, time_now):
    
    cv2.circle(frame, center, radius, (255, 255, 255), 1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(1,13):
        angle = math.radians(i * 30)
        x = int(center[0] + 0.8 * radius * math.sin(angle) - 10)
        y = int(center[1] - 0.8 * radius * math.cos(angle) + 5)  # Change the y-coordinate to adjust the position
        cv2.putText(frame, str(i), (x, y), font, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    
    # 360/12=30, 30/60seconde=0.5
    draw_hand(frame, center, radius * 0.6, math.radians(time_now.tm_hour * 30 + time_now.tm_min * 0.5 - 90), 8, (0, 0, 2550)) 
    draw_hand(frame, center, radius * 0.8, math.radians(time_now.tm_min * 6 - 90), 4, (255, 0, 0))
    draw_hand(frame, center, radius * 0.9, math.radians(time_now.tm_sec * 6-90), 2, (0, 0, 0))

def draw_hand(frame, center, length, angle, thickness, color):
    x2 = int(center[0] + length * math.cos(angle))
    y2 = int(center[1] + length * math.sin(angle))
    cv2.line(frame, center, (x2, y2), color, thickness)

def main():
    
    window_size = 500
    center = (int(window_size / 2), int(window_size / 2))
    radius = int(window_size / 2) - 20

    
    clock_frame = np.zeros((window_size, window_size, 3), dtype=np.uint8)

    while True:
        
        current_time = time.localtime()

        # Draw the clock
        draw_clock(clock_frame, center, radius, current_time)

        
        cv2.imshow("Analog Clock", clock_frame)

        
        key = cv2.waitKey(100)

        
        if key == 27:  
            break

    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
