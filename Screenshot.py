import pyautogui
import time
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'D:/My Learning/PROJECTS/python_practice/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()



root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text="Take Screenshot",command=screenshot)


button.pack(side=tk.LEFT)
close = tk.Button(frame,text="Quit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()