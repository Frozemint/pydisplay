import sys,os
import curses
import time
import forecastiopy
import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta

def draw_app(stdscr):
    #clear screen
    key = 0
    height, width = stdscr.getmaxyx() #get window height width
    stdscr.clear() #clear screen
    stdscr.refresh()

    curses.curs_set(0) #cursor to invisible
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) #title bar, TEXTCOLOR, BACKGROUNDCOLOR
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while True:
        try: 
            stdscr.clear()

            #get and ready all fields
            statusbarstr = "Infomation Board"
            statusbarsubtitlestr = "* * Live Timing and Status Information * *"
            time_string = time.strftime('%Y %B %dth (%A), %H:%M:%S.' + str(int(round(time.time() * 1000)))[-3:] + ' %Z') 
            hong_kong = timezone('Asia/Hong_Kong')
            hong_kong_now = datetime.datetime.now(hong_kong)
            intl_time_string = time.strftime('%Y %B %d %H:%M:%S GMT', time.gmtime()) + " ---- " +  hong_kong_now.strftime('%H:%M:%S %Z')

            today = datetime.datetime.now()
            day0 = datetime.datetime(2018, 9, 7, 15, 0, 0, 0) #magic date 
            day00 = datetime.datetime(1998, 12, 7, 7, 0, 0, 0) 
            current_age = relativedelta(today, day0)
            current_age = str(current_age.years) + " years " + str(current_age.months) + " months " + str(current_age.days) + " days " + str(current_age.hours) + " hours " + str(current_age.minutes) + " minutes " + str(current_age.seconds) + "." + str(current_age.microseconds//100000) + " seconds "
            outlive_day0 = datetime.datetime(2038, 6, 8, 23, 0, 0, 0)
            outlive_time = relativedelta(today, outlive_day0)
            outlive_time = str(outlive_time.years) + " years " + str(outlive_time.months) + " months " + str(outlive_time.days) + " days " + str(outlive_time.hours) + " hours " + str(outlive_time.minutes) + " minutes " + str(outlive_time.seconds) + "." + str(outlive_time.microseconds//100000) + " seconds "
            current_uptime = relativedelta(today, day00)
            current_uptime = current_uptime = str(current_uptime.years) + " years " + str(current_uptime.months) + " months " + str(current_uptime.days) + " days " + str(current_uptime.hours) + " hours " + str(current_uptime.minutes) + " minutes " + str(current_uptime.seconds) + "." + str(current_uptime.microseconds//100000) + " seconds "
            #title bar sector
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(0, 0, " " * ((width - len(statusbarstr))//2) + statusbarstr + " " * ((width - len(statusbarstr))//2))
            stdscr.attroff(curses.color_pair(1))

            #text under the title bar
            stdscr.addstr(1, 0, " " * ((width - len(statusbarsubtitlestr))//2) + statusbarsubtitlestr + " " * ((width - len(statusbarsubtitlestr))//2))

            #current time field
            stdscr.addstr(3, 0, "Current time: ", curses.color_pair(2))
            stdscr.addstr(3, 14, time_string)

            #int'l time field
            stdscr.addstr(4, 0, "Current GMT: ", curses.color_pair(2))
            stdscr.addstr(4, 13, intl_time_string)

            #divider 
            stdscr.addstr(5, 0, "--------------")

            #age field
            stdscr.addstr(7, 0, "Your age: ", curses.color_pair(3))
            stdscr.addstr(7, 10, current_age)

            #uptime field
            stdscr.addstr(8, 0, "Your uptime: ", curses.color_pair(3))
            stdscr.addstr(8, 13, current_uptime)

            #outlive field
            stdscr.addstr(9, 0, "You are projected to outlive the superceded person in: ", curses.color_pair(4))
            stdscr.addstr(10, 0, outlive_time)

            #divider 
            stdscr.addstr(12, 0, "--------------")

            #current weather field
            stdscr.addstr(14, 0, "Current Weather: ", curses.color_pair(2))


            stdscr.refresh() #refresh screen
            time.sleep(0.01) #needed or else screen does not refresh

        except KeyboardInterrupt:
            return



def main():
    curses.wrapper(draw_app)

def initWeatherAPI():
    qePark = [49.241753, -123.115268] #https://en.wikipedia.org/wiki/Queen_Elizabeth_Park,_British_Columbia
    apiKey = open("key.txt", "r")
    apiKey = apiKey.readLine()
    forecast = ForecastIO.ForecastIO(apiKey, latitude=qePark[0], longitude=qePark[1])

if __name__ == "__main__":
    main()
