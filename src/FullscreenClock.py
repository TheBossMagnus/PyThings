import tkinter as tk
import keyboard
import datetime
import psutil


def fullscreenclock():
    def kill():
        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                proc.kill()
    keyboard.add_hotkey("ctrl+shift+z", kill)
    def update_clock():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        lab.config(text=current_time, font=('Segoe UI (TrueType)', 250, 'bold'))
        win.after(1000, update_clock)

    win = tk.Tk()
    win.wm_attributes("-fullscreen", True)
    lab = tk.Label(win, text="00:00:00")
    lab.pack()

    update_clock()
    win.mainloop()
