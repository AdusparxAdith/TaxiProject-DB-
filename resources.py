import time
import random
# JUST A RANDOM SCRIPT FOR COMMONLY USED FUNCTIONS TO AVOID CLUTTER
def line():
    print("-"*120)

def Timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        print(timeformat, end='\r')
    print('Your ride has arrived!\n\n')
    print('Please submit',random.randint(1000,9999),'as the OTP')
