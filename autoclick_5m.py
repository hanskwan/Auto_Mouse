import pyautogui as pg
import time

pg.FAILSAFE = True

# separation for one click n in minutes
minutes_per_click = 5 # in minutes
pause_time = minutes_per_click*60 # in seconds 
repeat_times = 100
duration = lambda x, y: x*y/60

# Repeat click program

print("This autoclick program will last for " + str(round(duration(minutes_per_click, repeat_times), 2)) + " hours")
print("Click rate: " + str(60*minutes_per_click) +"seconds per click")
for i in range(repeat_times):
    pg.click()
    print(i)
    time.sleep(pause_time)
    
