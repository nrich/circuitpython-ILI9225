import board
import busio
import digitalio

from TFT_22_ILI9225 import TFT_22_ILI9225

# Example to connect a RaspberryPI Pico board to ILI9225 display.

spi = busio.SPI(board.GP10, board.GP11)
while not spi.try_lock():
    pass
spi.configure(baudrate=40000000)
spi.unlock()

lcd = TFT_22_ILI9225(spi, dc=board.GP8, cs=board.GP9, rst=board.GP0)
