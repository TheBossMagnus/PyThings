import tkinter  as tk
from pick import pick
import datetime

# --- Mini-clock ---

def widgetclock():
    def update_clock():
        # get current time as text
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # udpate text in Label
        lab.config(text=current_time, font=('Segoe UI (TrueType)',12))
        #lab['text'] = current_time

        # run itself again after 1000 ms
        win.after(1000, update_clock)

    #https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
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

def FullscreenCloclk():
    def update_clock():
        # get current time as text
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # udpate text in Label
        lab.config(text=current_time, font=('Segoe UI (TrueType)',250, 'bold'))
        #lab['text'] = current_time

        # run itself again after 1000 ms
        win.after(1000, update_clock)

    #https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
    def center_window(w=65, h=20):
        # get screen width and height
        hs = win.winfo_screenheight()
        # calculate position x, y
        x = 0
        y = (hs/1.085)
        win.geometry('%dx%d+%d+%d' % (w, h, x, y))

    win = tk.Tk()
    #center_window(65, 20)
    #win.overrideredirect(True)
    #win.wm_attributes('-topmost', 'True')
    win.wm_attributes("-fullscreen", True)
    lab = tk.Label(win, text="00:00:00")
    lab.pack()

    update_clock()
    win.mainloop()

#FullscreenCloclk()

def Menu():
    title = 'Pyclock by TheBossMagnus'
    options = ['Widget clock','Fullscreen clock','Widget timer','Fullscreen timer','exit']
    option, options = pick(options, title)

    if option == 'Widget clock':
        widgetclock()
        Menu()
    if option == 'Fullscreen clock':
        FullscreenCloclk()
        Menu()
    if option == 'Widget timer':
        print('SOON')
        Menu()
    if option == 'Fullscreen timer':
        print('SOON')
        Menu()
    if option == 'exit':
        exit()

Menu()