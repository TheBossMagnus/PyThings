 # thanks to https://youtu.be/kfjdVgKE6xY for threading
import tkinter as tk
import keyboard
import datetime
import time
import threading
import sys
import playsound
import psutil


class timer():
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
