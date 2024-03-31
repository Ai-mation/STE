import cv2
import numpy as np
from PIL import ImageGrab
import pygetwindow as gw
import time

def capture_screen(bbox=None):
    # Capture the screen
    screenshot = ImageGrab.grab(bbox)
    # Convert the screenshot to a numpy array
    frame = np.array(screenshot)
    # Convert from BGR (OpenCV's format) to RGB (PIL's format)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

def main():
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 10.0, (gw.getScreenSize()))

    start_time = time.time()
    duration = 10 # seconds

    while int(time.time() - start_time) < duration:
        frame = capture_screen()
        # Write the frame
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Break loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
