from time import ctime
import calendar
import datetime
import ntplib


def timestats():
    response = ntplib.NTPClient().request('pool.ntp.org')
    output= response.tx_time
    converted=ctime(output)

    weekday, month, day, time, year =converted.split()
    hours, minutes, seconds = time.split(':')

    if weekday == 'Mon':
        weekday = 'Monday'
    elif weekday == 'Tue':
        weekday = 'Tuesday'
    elif weekday == 'Wed':
        weekday = 'Wednesday'
    elif weekday == 'Thu':
        weekday = 'Thursday'
    elif weekday == 'Fri':
        weekday = 'Friday'
    elif weekday == 'Sat':
        weekday = 'Saturday'
    elif weekday == 'Sun':
        weekday = 'Sunday'

    if month == 'Jan':
        month = 'January'
    elif month == 'Feb':
        month = 'February'
    elif month == 'Mar':
        month = 'March'
    elif month == 'Apr':
        month = 'April'
    elif month == 'May':
        month = 'May'
    elif month == 'Jun':
        month = 'June'
    elif month == 'Jul':
        month = 'July'
    elif month == 'Aug':
        month = 'August'
    elif month == 'Sep':
        month = 'September'
    elif month == 'Oct':
        month = 'October'
    elif month == 'Nov':
        month = 'November'
    elif month == 'Dec':
        month = 'December'

    print(f"Today is {weekday} {day} {month} {year}" )
    print(f"It's {time}\n")

    today = datetime.date.today()
    days_in_current_month = calendar.monthrange(today.year, today.month)[1]
    days_till_end_month = days_in_current_month - today.day
    print("There are", 365 - today.timetuple().tm_yday, "days till the end of the year")
    print("There are", 52 - today.isocalendar()[1], "weeks till the end of the year")
    print("There are", 12 - today.month, "months till the end of the year\n")

    print(f"There are {days_till_end_month} days till the end of the month")
    print(f"There are {days_till_end_month//7} weeks till the end of the month\n")

    print("There are", 7 - today.weekday(), "days till the end of the week")



