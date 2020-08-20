#!/usr/bin/env python
# A simple timer program used to feed Mags

import time
from playsound import playsound

seconds = 45
while seconds > 0:
    if seconds == 30:
        print("30 seconds to go...")
    if seconds == 1:
        playsound('C:/Users/kamik/code/projects/pso_timer/sounds/jingle.wav')

    time.sleep(1) # every second
    seconds -= 1 # remove one second
