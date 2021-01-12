from machine import Pin
from neopixel import NeoPixel
from time import sleep

n = 60
np = NeoPixel(Pin(4), 60)

def solid(r, g, b):
    for i in range(60):
        np[i] = (r, g, b)
    np.write()

def bounce(r, g, b, wait):
    for i in range(10 * n):
        for j in range(n):
            np[j] = (r, g, b)

        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        sleep_ms(wait)

def cycle(r, g, b, wait):
    for i in range(10 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
            np[i % n] = (r, g, b)
        np.write()
        sleep_ms(wait)

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(n):
            rc_index = (i * 256 // n) + j
            np[i] = wheel(rc_index & 255)
        np.write()
        sleep_ms(wait)
