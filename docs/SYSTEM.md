# Funcionamiento del sistema de control

En este documento encontrarás la explicación del funcionamiento del sistema principal que controla el circuito.

## Diagrama de funcionamiento

Aquí tienes una idea más general de cómo funciona el circuito en forma de diagrama:

<img src="/docs/images/system/systemDiagram.svg" width="600">

Como puedes ver hay un proceso de escucha en bucle que toma los valores de los que nos proveen los sensores integrados en el circuito (BME280 y SCT-013). Ese bucle de escucha a su vez actúa de emisor para los actuadores (ventiladores) y elementos de monitorización (panel OLED) de nuestro circuito.

Como la información se extrae y se '*inyecta*' en los demás elementos, no se guarda ninguna referencia adicional en memoria a estos datos. Esto hace que el sistema sea más eficiente en recursos.
También, al condensar el proceso en un sólo sistema periódico estamos gastando menos recursos al condensarlos en un sólo proceso paralelo.

## Explicación del código

Vamos a echar un vistazo al código del archivo `main.py`, explicando por bloques de código lo que se va haciendo y con qué intención se realiza.

#### 1. Importando las librerías

```python
from machine import Pin, Timer, SoftI2C
from bme280 import BME280
from ssd1306 import SSD1306_I2C
```

Al inicio del código, como en la mayoría de scripts para la placa que estamos utilizando, importaremos algunas clases de la librearía `machine` (Documentación en inglés de la librería ~> https://docs.micropython.org/en/latest/library/machine.html).

En este caso:

- Importamos la clase `Pin` para poder interactuar con los ventiladores, cambiado el valor de salida del Pin donde vaya contectado el input del módulo de relé doble. 
- Importamos la clase `Timer` para crear el *bucle de escucha* representado en el diagrama de funcionamiento.
- Importamos la clase `SoftI2C` para poder comunicarnos con el sensor BME280 y la panel OLED. Utilizamos esta clase puesto que su clase predecesora, `I2C` ya está obsoleta en esta librería.


#### 2. Definiendo las instancias de los módulos

```python
i2cbus = SoftI2C(scl=Pin(22), sda=Pin(21))
bme280 = BME280(i2c=i2cbus)
oled = SSD1306_I2C(width=128, height=64, i2c=i2cbus)
# sct013 = ...

fans_output = Pin(12, Pin.OUT)
```

No entraré mucho en detalle, pero dado que tanto la pantalla OLED como el sensor BME280 se comunican con la placa por el protocolo I2C, debemos crear un ***bus de datos***  por el cual podamos enviar y recibir información de ambos elementos a la vez mediante los pines 22 (scl) y 21 (sda). 
Esto podemos hacerlo sacando dos cables a cualquier parte de la *protoboard* y conectando dos paresde ellos en serie.

Una vez hemos declarado el bus I2C, podemos definir las variables `bme280` y `oled` que guardan instancias de su clase correspondiente. 

Simplemente a la instancia de `BME280` le pasamos al argumento `i2c` la referencia al bus I2C que hemos declarado antes. (Más información sobre la librería ~> https://github.com/robert-hh/BME280).

Y a la instancia de SSD1306_I2C (clase que nos facilita la comunicación con la pantalla OLED), le pasamos unos parámetros para la altura y anchura de la pantalla (en el caso de nuestra OLED 128x64) y también le pasamos una referencia del bus I2C de antes, al igual que en la instancia del BME280. (Más información sobre la OLED ~> https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html).

Después declaramos una varible que guardará una referencia para el pin que controle la entrada para el relé donde conectemos los ventiladores dentro del módulo de doble relé.


#### 3. Definiendo algunas constantes

Esta sección del código está creada para definir valores inmutables a lo largo del proceso de ejecución. Esto quiere decir que estamos definiendo valores fijos que nos servirán en el código para hacer más claras algunas de sus partes.

`TEMP_IDX`, `PRES_IDX`, `HUM_IDX`; son constantes que identifican el índice de los valores que obtenemos de la tupla que devuelve la librería del sensor BME280. Declarando estas constantes podemos ver mejor de dónde vienen estos valores.

`MIN_TEMP`, `MAX_TEMP`; son valores de temperatura que utilizaremos a la hora de comprar la temperatura de la habitación en la que nos encontremos y accionar o no los ventiladores.


#### 4. Definiendo las funciones que integra el *listener* o bucle de escucha:

```python
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
```

Aquí tenemos dos funciones que se ejecutarán periódicamente en la función `listener` que estamos utilizando como *callback* para nuestro `Timer`.

La primera función `update_oled()` toma los valores del sensor BME280, utilizando la propiedad `values`, que nos devuelve una tupla de enteros (*tuple[int]*), y las muestra en distintas secciones de la pantalla OLED.
Además, puesto que tenemos espacio suficiente podemos mostrar los valores de temperatura máxima y mínimas que hemos definido antes en las [constantes](#3-definiendo-algunas-constantes). 
Para que los valores de la pantalla OLED no se superpongan, estamos refrescando la pantalla por cada ciclo del bucle de escucha rellenando la pantalla completamente de color negro tras mostrar los valores que le estamos escribiendo.

> **Note:** El valor de retorno de la propiedad values de la librearía BME280 está modificado para adaptarse al proyecto.
>
> - Original:
> ```python
>    @property
>    def values(self):
>        """ human readable values """ 
>
>        t, p, h = self.read_compensated_data()
>
>        return ("{:.2f}C".format(t), "{:.2f}hPa".format(p/100), 
>                "{:.2f}%".format(h))
>```
>
>- Modificado:
>```python
>    @property
>    def values(self):
>        """ human readable values """ # Modified it to return a tuple[int] instead of a tuple[str]
>
>        t, p, h = self.read_compensated_data()
>
>        return (round(t, 2), round(p/100, 2), round(h, 2))
>```

Y la segunda función por su sencillez está definida en una sóla línea. Las funciones que definimos en línea son las denominadas funciones *lambda*, de ahí la palabra clave que se utiliza para definirlas. Por lo general toman uno o más paramétros, puesto que este tipo de funciones está pensada para devolver lo que se especifique en la expresión que incluyamos en la función. En este caso, como no estamos devolviendo la función, si fuéramos a mostrar en consola el resultado sería `None`.
(Más información sobre las funciones lambda ~> https://docs.python.org/3/reference/expressions.html#lambdas).

En esta función, cambiamos el valor de salida de los ventiladores a través de una condición.
Esta condición puede devolver dos valores *booleanos*: `True` o `False`.
Puesto que la función `value()` de la clase Pin acepta valores booleanos como parámetro (referencia en la documentación ~> https://docs.micropython.org/en/latest/library/machine.Pin.html?highlight=pin#machine.Pin), podemos utilizar el valor de retorno de esa condición para encender o apagar los ventiladores comparando la temperatura de la habitación con la máxima temperatura permitida (`MAX_TEMP`).
Sin embargo, debemos tener en cuenta que los relés del módulo que estamos utilizando se activan por **baja**, por lo que tenemos que invetir el resultado con `not` para obtener el comportamiento correcto.

*Al definir las funciones por separado hacemos el código un poco más legible para un tercero.*

#### 5. Declarando el *listener* o bucle de escucha.

```python
def listener(t):
    update_oled()
    update_fans()

listener_handler = Timer(0)
listener_handler.init(period=500, callback=listener)
```

Ahora que tenemos las funciones que va a integrar nuestro bucle de escucha, podemos llamarlas dentro del *callback* que ejecuta el `Timer`. Una función *callback* es aquella que se pasa como paramétro para una función o clase para ser posteriormente ejecutada.  

En este caso, la función que va a ejecutar el `Timer` se llama `listener()` y acepta un como parámetro una referencia de la clase `Timer` (*Esto puede ser útil para detener un proceso definido como periódico, tras un número concreto de iteraciones*).

Una vez tenemos la función, definimos el `Timer` encargado de ejecutar dicho proceso cada cierto tiempo de forma periódica. En este caso, tiene el nombre de `listener_handler`.
Para poder definir una instancia de la clase `Timer`, primero debemos asignarle un número de identificación o ID (*En el caso de la placa ESP32 contamos con 4 timers cuyos IDs van del 0 al 3*).
Después, utilizando la función `init()` de la clase `Timer`, modficaremos las características del Timer a nuestras necesidades.

Para el tipo de bucle que queremos construir, dado que el Timer ejecuta la función *callback* de forma periódica por defecto, sólamente tendremos que especificar cada cuanto queremos que se ejecute nuestro *callback*. Esto lo hacemos pasándole en esta ocasión el número `500` al argumento `period`. La unidad de medida del periodo está en `ms`.
Por último, le pasamos al argumento `callback` el nombre de nuestra función `listener()`.

Ese es el funcionamiento básico del sistema.
