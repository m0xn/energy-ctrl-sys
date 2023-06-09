from machine import Pin, Timer, SoftI2C
from bme280 import BME280
from ssd1306 import SSD1306_I2C

"""
Final script for the power consmption project
author: Rodrigo (Moon)
license: MIT
"""

sensor_vals = {
    "BME280": None,
    "SCT-013": None
}

TEMP_IDX = 0
PRES_IDX = 1
HUM_IDX = 2

i2c_bus = SoftI2C(scl=Pin(22), sda=Pin(21))

bme280 = BME280(i2c=i2c_bus)
oled = SSD1306_I2C(128, 64, i2c_bus)
oled.poweron()
# acsensor = ...

fan_output = Pin(14, Pin.OUT)
temp_threshold = 25.0

fan_output.on()

def bme_format(values: tuple[int]) -> tuple[str]:
    return (f'{values[TEMP_IDX]}C', f'{values[PRES_IDX]}hPa', f'{values[HUM_IDX]}%')

def temp_listen(t):
    global sensor_vals
    fan_output.value(1 if float(sensor_vals["BME280"][TEMP_IDX]) > temp_threshold else 0)
                     
def update(t):
    global sensor_vals
    
    sensor_vals["BME280"] = bme280.values
    # sensor_vals["SCT-013"] = acsensor.values
    
    # oled.text(f"W: {sensor_vals["SCT-013"][0]}", 0, 0, 1)
    oled.text(f"TEMP: {sensor_vals["BME280"][TEMP_IDX]}C", 0, 16, 1)
    oled.text(f"PRES: {sensor_vals["BME280"][PRES_IDX]}hPa", 0, 32, 1)
    oled.text(f"HUM: {sensor_vals["BME280"][HUM_IDX]}%", 0, 48, 1)
    
    oled.show()
    oled.fill(0)

updater = Timer(0)
updater.init(period=500, callback=update)

fan_listener = Timer(1)
fan_listener.init(period=500, callback=temp_listen)