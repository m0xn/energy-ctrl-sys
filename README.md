# Sistema de gestión de energía

*TODO: Queda por implementar el sensor SCT-013 dentro del circuito, por lo que los sistemas aún están incompletos*

## Tabla de contenidos

- [Introducción](#introducción)
- [Componentes](#componentes)
- [Montaje](#montaje)
- [Scripts]()

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
| Microcontrolador ESP32 | <img src="/images/modules/esp32.jpg" width="200"> | LEDs (uno rojo y uno verde) | <img src="/images/modules/leds.jpg" width="200"> |
| BME280 | <img src="/images/modules/bme280.jpg" width="200"> | SCT-013 | <img src="/images/modules/sct-013.jpg" width="200"> |
| Cables | <img src="/images/modules/cables.jpg" width="200"> | Ventiladores (x2) | <img src="/images/modules/fans.jpg" width="200"> |  
| Relé doble | <img src="/images/modules/doubleRelay.jpg" width="200"> | panel OLED | <img src="/images/modules/oledPanel.jpeg" width="200">

## Montaje

Aquí está una referencia de cómo debería quedar el circuito básico:

![](/images/baseCircuit.jpg)


## Scripts

#### Librerías

Este proyecto utiliza algunas librerías externas para poder establecer comunicación con algunos de los elementos del circuito (OLED, BME280 y ~~SCT-013~~).
Dichas librerías están localizadas en el dicrectorio `libs/` del repositorio.

Para poder utilizarlas deberás instalarlas en tu placa ESP32.

Esto puede hacerse de dos formas:

1. Utilizando Thonny:

Esta es la forma más fácil de escribir un copia del archivo dentro de la placa.

- Primero, deberás tener abierto el archivo que quieres guardar dentro de la placa abierto en el editor. Pongamos como ejemplo el archivo `main.py` del repositorio:

<img src='/images/thonny/screenshot1.png' width="700">
