import cv2
import numpy as np
import pyautogui
import time
import sys
import os
import gi
gi.require_version('Wnck','3.0')
from gi.repository import Wnck
import psutil
from tkinter import *
from tkinter.filedialog import asksaveasfilename

def rec():
    #Recording Function
    screen_size = pyautogui.size()
    filename = asksaveasfilename(confirmoverwrite=False,defaultextension='.avi')
    fourcc=cv2.VideoWriter_fourcc(*"XVID")
    out=cv2.VideoWriter(filename,fourcc,20.0,(screen_size))

    while True:
        screen = Wnck.Screen.get_default()
        screen.force_update()
        windows=screen.get_windows()
        for w in windows:
            if 'show' in w.get_name():
                w.minimize()

        img=pyautogui.screenshot()
        frame=np.array(img)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("show",frame)

        if cv2.waitKey(1)==ord("q"):
            c = psutil.Process(pid=os.getpid())
            c.terminate()
            break
#Screenshot Function
def ss():
    time.sleep(1)
    ss=pyautogui.screenshot()
    filename =asksaveasfilename(confirmoverwrite=False,defaultextension='.png')
    ss.save(filename)
def exitall():
    # c = psutil.Process(pid=os.getpid())
    # c.terminate()
    sys.exit(0)
if __name__ == "__main__":
    #Tkinter GUI Basic
    root = Tk()
    root.title("Screen Recorder")
    root.geometry("800x150")

    #Other Properties
    frame = Frame(root,pady=1,padx=1, borderwidth=5)
    frame.grid(row=0,column=0)
    sr = Button(frame,text="Record",font="lucida 15 italic",command=rec)
    sr.grid(row=1,column=4)
    scrnsht = Button(frame,text="Screenshot",font="lucida 15 italic",command=ss)
    scrnsht.grid(row=2,column=4)
    quitbtn = Button(frame,text="Quit",command=exitall)
    quitbtn.grid(row=3,column=10)
    root.mainloop()