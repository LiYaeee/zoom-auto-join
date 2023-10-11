import webbrowser
import schedule
import time
from links import *


#variables to open chrome as default browser
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

c = webbrowser.get('chrome')


# Function to open the web page
def fil():
    c.open(FIL)

def ds101():
    c.open(DS101)

def actg():
    c.open(ACTG)

def mst():
    c.open(MST)

def cc_104():
    c.open(CC104)

def pe():
    c.open(PE)

def sdf104():
    c.open(SDF104)

def ias101():
    c.open("ti")

def fb():
    print("ae")

schedule.every().wednesday.at("07:00").do(fb)
schedule.every().wednesday.at("10:00").do(actg)
schedule.every().wednesday.at("11:00").do(ds101)
schedule.every().wednesday.at("07:00").do(cc_104)

i = 0
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)



