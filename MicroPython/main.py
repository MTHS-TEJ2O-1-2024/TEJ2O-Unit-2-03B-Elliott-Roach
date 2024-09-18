"""
Created by: Elliott
Created on: Sep 2024
This module is a Micro:bit MicroPython program calculats area and primiter
"""

from microbit import *

display.clear()
sleep(1)


display.scroll("Area =" + str(5 * 3))

sleep(1)
display.clear()
sleep(1)

display.scroll("Primiter =" + str(2 * (2 + 3)))
