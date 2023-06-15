from machine import Pin, Timer, SoftI2C
from bme280 import BME280
from ssd1306 import SSD1306_I2C

i2cbus = SoftI2C(scl=Pin(22), sda=Pin(21))
bme280 = BME280(i2c=i2cbus)
oled = SSD1306_I2C(width=128, height=64, i2c=i2cbus)
# sct013 = ...

fans_output = Pin(12, Pin.OUT)

# Constants

TEMP_IDX = 0
PRES_IDX = 1
HUM_IDX = 2
MIN_TEMP = 20
MAX_TEMP = 28

def update_oled():
    # oled.text(f'POWER: {sct013.values[0]}W', 0, 0)

    oled.text(f'TEMP: {bme280.values[TEMP_IDX]}C', 0, 9)
    oled.text(f'MIN: {MIN_TEMP}C', 0, 18)
    oled.text(f'MAX: {MAX_TEMP}C', 0, 27)

    oled.text(f'PRES: {bme280.values[PRES_IDX]}hPa', 0, 36)
    oled.text(f'HUM: {bme280.values[HUM_IDX]}%', 0, 45)

    oled.show()
    oled.fill(0)

update_fans = lambda: fans_output.value(not bme280.values[TEMP_IDX] > MAX_TEMP) # Relay actives on low, therefore, the condition is inverted with 'not'

def listener(t):
    update_oled()
    update_fans()

listener_handler = Timer(0)
listener_handler.init(period=500, callback=listener)
