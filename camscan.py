import cv2
import tkinter as tk
from tkinter import simpledialog

cam = cv2.VideoCapture(0)

cv2.namedWindow("cam_feed")

while(True):
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame.")
        break
    cv2.imshow("cam_feed", frame)
    
    k = cv2.waitKey(1)
    if k%256 == 27:         # ESC pressed
        print("closing...")
        break
    elif k%256 == 32:       # SPACE pressed
        ROOT = tk.Tk()
        ROOT.withdraw()
        USER_INP = simpledialog.askstring(title="name",prompt="Name: ")

        img_name = "{}.png".format(USER_INP)
        cv2.imwrite(img_name, frame)
        print("{} written".format(img_name))

cam.release()
cv2.destroyAllWindows()
