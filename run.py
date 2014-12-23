from time import sleep
from collect import collect
from parameters import SECONDS_IN_MINUTE
from publish import Publishing

while True:
    collect()
    Publishing().publish()
    minutes = 15
    print("Will sleep for %d minutes" % minutes)
    sleep(minutes * SECONDS_IN_MINUTE)