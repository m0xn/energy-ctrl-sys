# Sistema de gestión de energía

## Tabla de contenidos

- [Introducción](#introducción)
- [Componentes](#componentes)
- [Montaje]()
- [Scripts]()
- [Sistema de control]()

## Introducción

Este repositorio recoge todos los recursos e instrucciones necesarios para montar un sistema básico de gestión de energía.

El sistema funciona de la siguiente forma:
    
- El sensor `SCT-013` se encarga de tomar los vatios consumidos por los dispositivos eléctricos enchufados a una regleta.
- Dichos dispositivos nos servirán como una fuente manual de calor con la que estaremos trabajando.
- Si la temperatura de la habitación donde nos encontremos supera un umbral superior de temperatura`MAX_TEMP`, los ventiladores se activarán.

Los valores con los que estaremos trabajando se mostrarán en la pantalla OLED, de esa forma monitorizando los valores obtenidos en un dispositivo fijo.

## Componentes 

| Nombre | Imagen | Nombre | Imagen |
| ------ | ------ | ------ | ------ |
| Microcontrolador ESP32 | <img src="/images/esp32.jpg" width="200"> | LEDs (uno rojo y uno verde) | <img src="/images/leds.jpg" width="200"> |
| BME280 | <img src="/images/bme280.jpg" width="200"> | SCT-013 | <img src="/images/sct-013.jpg" width="200"> |
| Cables | <img src="/images/cables.jpg" width="200"> | Ventiladores (x2) | <img src="/images/fans.jpg" width="200"> |  
| Relé doble | <img src="/images/doubleRelay.jpg" width="200"> | panel OLED | <img src="/images/oledPanel.jpeg" width="200">

