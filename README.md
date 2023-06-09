# Sistema de monitorización de consumo eléctrico 

En este repositorio podrás encontrar todos los **recursos** necesarios para montar un *sistema básico de monitorización de consumo eléctrico*.

## Tabla de contenidos

- [Componentes](#componentes)
- [Librerías](#librerias)

## Componentes 

| Nombre | Imagen | Nombre | Imagen |
| ------ | ------ | ------ | ------ |
| Microcontrolador ESP32 | <img src="/images/esp32.jpg" width="200"> | LEDs (uno rojo y uno verde) | <img src="/images/leds.jpg" width="200"> |
| BME280 | <img src="/images/bme280.jpg" width="200"> | SCT-013 | <img src="/images/sct-013.jpg" width="200"> |
| Cables | <img src="/images/cables.jpg" width="200"> | Ventiladores (x2) | <img src="/images/fans.jpg" width="200"> |  
| Relé doble | <img src="/images/doubleRelay.jpg" width="200"> | panel OLED | <img src="/images/oledPanel.jpeg" width="200">

## Librerías

Para poder establecer una comunicación a mayor nivel con ciertos componentes del circuito necesitamos una serie de librerías concretas. En concreto, necesitamos librerías para los siguientes componentes:

- BME280 ~> `imges/bme280.py`
- SCT-013 ~> *falta por implementar*
- OLED -> `images/ssd1306.py`


