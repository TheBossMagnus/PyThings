import tkinter as tk
import datetime
import keyboard
import psutil


def widgetclock():
    def kill():
        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                proc.kill()
    keyboard.add_hotkey("ctrl+shift+z", kill)
    def update_clock():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        lab.config(text=current_time, font=('Segoe UI (TrueType)', 12))
        win.after(1000, update_clock)

    # https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
    def center_window():
        hs = win.winfo_screenheight()
        y = round(hs/1.085) #because win.geometry don't love decimals
        win.geometry(f"65x20+0+{y}")

    win = tk.Tk()
    center_window()
    win.overrideredirect(True)
    win.wm_attributes('-topmost', 'True')
    lab = tk.Label(win, text="00:00:00")
    lab.pack()

    update_clock()
    win.mainloop()
