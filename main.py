import cv2
import os
import time
from datetime import datetime

FOLDER_TO_WATCH = os.path.expanduser("~/Desktop/exercises")
PHOTO_SAVE_FOLDER = os.path.expanduser("~/Desktop/camerapassword/captured_images")

def take_picture():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        os.makedirs(PHOTO_SAVE_FOLDER, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"photo_{timestamp}.png"
        cv2.imwrite(os.path.join(PHOTO_SAVE_FOLDER, filename), frame)
        print(f"[+] Photo taken: {filename}")
    cam.release()

def start_monitoring():
    print(f"Monitoring folder access: {FOLDER_TO_WATCH}")
    last_access_time = os.stat(FOLDER_TO_WATCH).st_atime

    try:
        while True:
            time.sleep(1)
            current_access_time = os.stat(FOLDER_TO_WATCH).st_atime
            if current_access_time != last_access_time:
                print("[*] Folder was accessed!")
                take_picture()
                last_access_time = current_access_time
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    start_monitoring()
