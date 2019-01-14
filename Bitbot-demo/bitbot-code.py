from microbit import *
import radio
import neopixel

neopixels= neopixel.NeoPixel(pin13, 12)
radio.on()

def set_neopixel_colour(red, green, blue):
    colour_val = (red, green, blue)
    for n in range(len(neopixels)):
        neopixels[n] = colour_val
    
def forward():
    pin0.write_digital(1)
    pin1.write_digital(1)
    set_neopixel_colour(0, 0, 255)
    neopixels.show()
    
def stop():
    pin0.write_digital(0)
    pin1.write_digital(0)
    neopixels.clear()
    
while True:
    msg = radio.receive()
    if msg:
        if msg == 'forward':
            forward()
        elif msg == 'stop':
            stop()
    sleep(10)