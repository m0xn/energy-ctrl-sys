# Sistema de gestión de energía

*TODO: Queda por implementar el sensor SCT-013 dentro del circuito, por lo que los sistemas aún están incompletos*

## Tabla de contenidos

- [Introducción](#introducción)
- [Componentes](#componentes)
- [Scripts](#scripts)
- [Sistema de control](#sistema-de-control)
- [Contribuir](#contribuir)

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
| Micro-controlador ESP32 | <img src="/docs/images/modules/esp32.jpg" width="200"> | LEDs (rojo x1 y verde x1) | <img src="/docs/images/modules/leds.jpg" width="200"> |
| BME280 | <img src="/docs/images/modules/bme280.jpg" width="200"> | SCT-013 | <img src="/docs/images/modules/sct-013.jpg" width="200"> |
| Cables | <img src="/docs/images/modules/cables.jpg" width="200"> | Ventiladores (x2) | <img src="/docs/images/modules/fans.jpg" width="200"> |  
| Relé doble | <img src="/docs/images/modules/doubleRelay.jpg" width="200"> | panel OLED | <img src="/docs/images/modules/oledPanel.jpeg" width="200">

## Scripts

#### Librerías

Este proyecto utiliza algunas librerías externas para poder establecer comunicación con algunos de los elementos del circuito (OLED, BME280 y ~~SCT-013~~).
Dichas librerías están localizadas en el dicrectorio `libs/` del repositorio.

Para poder utilizarlas deberás instalarlas en tu placa ESP32.

Esto puede hacerse de dos formas:

1. **Utilizando Thonny**:

Esta es la forma más fácil de escribir un copia del archivo dentro de la placa.

(*Asegúrate de tener la placa conectada para seguir el proceso*)

- Primero, deberás tener abierto el archivo que quieres guardar dentro de la placa abierto en el editor. Pongamos como ejemplo el archivo `main.py` del repositorio:

<img src='/docs/images/thonny/screenshot1.png' width="900">

- Después, puedes dirigirte a `Fichero > Guardar` o `Fichero > Guardar como` (Si el archivo ya existe en el sistema). También puedes utilizar los atajos de teclado respectivos: `Ctrl+S`, 'Guardar'; `Ctrl+Shift+S`, 'Guardar como'.
Si es la primera vez que estas escribiendo el archivo en tu sistema, o si le das a 'Guardar como', te aparecerá la siguiente ventana emergente:

<img src='/docs/images/thonny/screenshot2.png' width="900">

- En vez de guardarlo en tu equipo, lo guardarás en tu placa ESP32 haciendo click en el botón con el texto '**Dispositivo MicroPython**'.

<img src='/docs/images/thonny/screenshot3.png' width="900">

- Para finalizar, escribes el nombre con el que quieras guardar el archivo y una vez le des a **Ok** tendrás el archivo escrito dentro de la memoria de la placa. 

2. **Utilizando una librería de python (ampy)**

Esta es otra alternativa para instalar scripts dentro de la placa a través de una librería de Python que es una aplicación de terminal que podemos ejecutar externamente. 

- Lo primero de todo es instalar la librería llamada '*ampy*' o como la podréis encontrar en PiPy '*adafruit-ampy*'. Aquí tenéis un enlace a la entrada de PiPy con la librería ~> https://pypi.org/project/adafruit-ampy/
Para instalar la librería tendréis que ejecutar el siguiente comando en la terminal:

```shell
pip install adafruit-ampy
```

- Una vez se haya instalado la librería, podremos llamar a la aplicación de consola *ampy* utilizando el comando `ampy`.

```shell
ampy
```

- Ejecutando este comando nos proporcionará una pequeña guía de ayuda para utilizar la librería.

- En nuestro caso, como nos intersa escribir archivos dentro de la placa, tenemos que especificar los siguientes parámetros:

    - `-p`: hace referencia al puerto serial por el que nos comunicamos con la ESP32. En el caso de Windows es `COM(N)` siendo N: 1,2,3,4... (*Podéis mirarlo en Thonny en la esquina inferior derecha*). En el caso de Linux, el puerto serial es un directorio dentro de `dev` llamado ttyUSB0 (`/dev/ttyUSB0`). 
    - `-b`: hace referencia a la tasa de *baud*. Este valor en la ESP32 es de **115200**.

(*El resto de parámetros no son tan relevantes*)

Después de los parámetros utilizaremos el método `put` para escribir un archivo dentro de la placa.

Por ejemplo, si fuéramos a escribir el archivo `bme280.py` dentro de la placa, pondríamos algo así:

(*Asumiendo que el archivo se encuentra en el directorio en el que estamos situados en terminal*)

**WINDOWS**:
```shell
ampy -p COM(N) -b 115200 put bme280.py 
```

**LINUX**:
```shell
ampy -p /dev/ttyUSB0 -b 115200 put bme280.py 
```

Tras unos segundos el archivo ya estará instalado en el dispositivo.
Hay que tener muy en cuenta que en este proceso NO puede haber una instancia de Thonny abierta. Esto es debido a que hay un conflicto al mandar datos a la placa porque el puerto serial que la conecta con nuestro equipo ya está ocupado por la instancia de Thonny. 

## Sistema de control

Puedes ver cómo funciona el sistema de control programdo en el archivo `main.py` en ~> [Sistema de control](/docs/SYSTEM.md)


## Contribuir

Para obtener más información sobre cómo contribuir con el proyecto, puedes dirigirte al archivo `CONTRIBUTING.md` ~> [Contribuir](/docs/CONTRIBUTING.md)
