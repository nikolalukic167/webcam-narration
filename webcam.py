import cv2
import time
import os

folder_path = "screenshots"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

save_interval = 5 
last_saved_time = time.time()
saved_frames = []

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0) # 0 is the default webcam

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)

    if time.time() - last_saved_time >= save_interval:
        last_saved_time = time.time()
        filename = os.path.join(folder_path, f"frame-{int(last_saved_time)}.jpg")
        cv2.imwrite(filename, frame)
        saved_frames.append(filename)
        print(f"Saved {filename}")

    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()

for filename in saved_frames:
    os.remove(filename)
    print(f"Deleted {filename}")

