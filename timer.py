#!/usr/bin/env python
# A simple timer program used to feed Mags

import time
min = int(input('>>'))
while min > 0:
    print(f"{min} minutes left..")
    time.sleep(60) # every minute
    min -= 1 # remove one minute 

