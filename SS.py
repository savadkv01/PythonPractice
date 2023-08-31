import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog, filedialog
from PIL import ImageGrab

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.button = tk.Button(self.frame, text="Capture Area", command=self.capture_area)
        self.button.pack(side=tk.LEFT)

        self.close = tk.Button(self.frame, text="Quit", command=self.root.quit)
        self.close.pack(side=tk.LEFT)

    def capture_area(self):
        self.root.iconify()  # Minimize the window during capture
        time.sleep(0.5)  # Wait for window to minimize

        im = ImageGrab.grab()  # Capture entire screen
        area = pyautogui.locateOnScreen("select_area.png")  # Replace with a custom selection indicator

        if area:
            x, y, width, height = area
            im = im.crop((x, y, x + width, y + height))

            name = simpledialog.askstring("Screenshot Name", "Enter a name for the screenshot:")
            if name:
                save_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=name)
                if save_path:
                    im.save(save_path)
                    im.show()
                    print(f"Screenshot saved as {save_path}")
                else:
                    print("Screenshot saving canceled.")
            else:
                print("Screenshot capture canceled")

        else:
            print("Could not find selection area indicator")

        self.root.deiconify()  # Restore the window after capture

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()