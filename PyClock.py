import tkinter as tk
import time
import datetime
import threading
from pick import pick
import playsound
import keyboard
import psutil

# --- Mini-clock ---


def widgetclock():
    def kill():
        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                proc.kill()
    keyboard.add_hotkey("ctrl+shift+z", kill)
    def update_clock():
        # get current time as text
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # update text in Label
        lab.config(text=current_time, font=('Segoe UI (TrueType)', 12))
        # lab['text'] = current_time

        # run itself again after 1000 ms
        win.after(1000, update_clock)

    # https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
    def center_window(w=65, h=20):
        # get screen width and height
        hs = win.winfo_screenheight()
        # calculate position x, y
        x = 0
        y = (hs/1.085)
        win.geometry('%dx%d+%d+%d' % (w, h, x, y))

    win = tk.Tk()
    center_window(65, 20)
    win.overrideredirect(True)
    win.wm_attributes('-topmost', 'True')
    lab = tk.Label(win, text="00:00:00")
    lab.pack()

    update_clock()
    win.mainloop()


 # thanks to https://youtu.be/kfjdVgKE6xY for threading
class Timer:
    def kill():
        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                proc.kill()
    keyboard.add_hotkey("ctrl+shift+z", kill)
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Timer")
        self.win.geometry("390x220")

        self.time_entry = tk.Entry(self.win) #Textbox
        self.time_entry.place(x=133, y=5, height=25)

        self.time_label = tk.Label(self.win, text="00:00:00", font = "Helvetica 70 bold") #time
        self.time_label.place(x=5, y=30)

        self.start_button = tk.Button(self.win, text="Start", font = "Helvetica 16", command=self.start_thread) #start
        self.start_button.place(x=90, y=165, height=30, width=60)

        self.stop_button = tk.Button(self.win, text="Stop", font = "Helvetica 16", command=self.stop) #stop
        self.stop_button.place(x=240, y=165, height=30, width=60)

        self.stop_loop = False

        self.win.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        hours, minutes, seconds = 0, 0, 0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])
        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print("Invalid input")
            return

        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.win.update()
            time.sleep(1)

        if not self.stop_loop:
            self.time_label.config(text="00:00:00")
            self.win.wm_attributes('-topmost', 'True')
            playsound.playsound("C:/Windows/Media/Alarm01.wav")  # use / instead of \ https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3

    def stop(self):
        self.stop_loop = True
        self.time_label.config(text="00:00:00")





def fullscreencloclk():
    def kill():
        for proc in psutil.process_iter():
            if proc.name() == "python.exe":
                proc.kill()
    keyboard.add_hotkey("ctrl+shift+z", kill)
    def update_clock():
        # get current time as text
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # update text in Label
        lab.config(text=current_time, font=('Segoe UI (TrueType)', 250, 'bold'))
        # lab['text'] = current_time

        # run itself again after 1000 ms
        win.after(1000, update_clock)

    # https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
    def center_window(w=65, h=20):
        # get screen width and height
        hs = win.winfo_screenheight()
        # calculate position x, y
        x = 0
        y = (hs/1.085)
        win.geometry('%dx%d+%d+%d' % (w, h, x, y))

    win = tk.Tk()
    # center_window(65, 20)
    # win.overrideredirect(True)
    # win.wm_attributes('-topmost', 'True')
    win.wm_attributes("-fullscreen", True)
    lab = tk.Label(win, text="00:00:00")
    lab.pack()

    update_clock()
    win.mainloop()

def Currenttime():
    #currentDateAndTime = datetime.now()
    print("The current date and time is")

def menu():
    title = 'Pyclock by TheBossMagnus'
    options = ['Widget clock', 'Fullscreen clock','Timer','Current time', 'exit']
    option, options = pick(options, title)

    if option == 'Widget clock':
        widgetclock()
        menu()
    if option == 'Fullscreen clock':
        fullscreencloclk()
        menu()
    if option == 'Timer':
        Timer()
        menu()
    if option == 'Current time':
        Currenttime()
        menu()
    if option == 'exit':
        exit()


menu()
