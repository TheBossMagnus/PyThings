import sys
from pick import pick
import WidgetClock
import FullscreenClock
import Timer
import TimeStats


def menu():
    title = 'RandomPyUtils by TheBossMagnus'
    options = ['Widget clock', 'Fullscreen clock','Timer','Current time', 'exit']
    option, options = pick(options, title)

    if option == 'Widget clock':
        WidgetClock.widgetclock()
        print("exit with control + shift + z")
    if option == 'Fullscreen clock':
        FullscreenClock.fullscreenclock()
        print("exit with control + shift + z")
    if option == 'Timer':
        Timer.timer()
    if option == 'Current time':
        TimeStats.timestats()
    if option == 'exit':
        sys.exit()


menu()
