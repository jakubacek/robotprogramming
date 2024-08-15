from neopixel import NeoPixel
from microbit import pin0
from microbit import sleep

# min led index
ledMin = 0

# max led index
ledMax = 8

# initialize led array
np = NeoPixel(pin0, 8)

# Zapni will set n led of array to white colour
def zapni(n):
    if validate(n):
        nastav_barvu(n, (255, 255, 255))


# Zapni will set n led of array to black colour
def vypni(n):
    if validate(n):
        nastav_barvu(n, (0, 0, 0))

# nastav barvu will set n led of array to specified colour
def nastav_barvu(n, colour):
    if validate(n):
        np[n] = colour
        np.write()

# led array boundary validation
def validate(n):
    return n >= 0 and n < 8


while True:
    zapni(0)
    sleep(1000)
    vypni(0)
    sleep(1000)
