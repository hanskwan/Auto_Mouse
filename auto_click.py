import pyautogui as pg
import datetime
import time
from tqdm import tqdm

pg.FAILSAFE = True

# separation for one click n in minutes
print("Enter how many seconds per click")
seconds_per_click_str = input()
seconds_per_click = int(seconds_per_click_str) # in secs
pause_time = seconds_per_click # in seconds

print("How long should auto-click last for in mins")
duration_str = input() # in mins
duration = int(duration_str)*60 # in secs


# Repeat click program

print("This autoclick program will last for " + duration_str + " mins")
print("Click rate: " + str(seconds_per_click) +" seconds per click")
for i in tqdm(range(duration)):
    pg.click()
    print("")
    print("Click", i," | " ,"Time", datetime.datetime.now().time())
    print("")
    time.sleep(pause_time)


    
