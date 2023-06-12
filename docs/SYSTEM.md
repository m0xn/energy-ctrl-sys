# Funcionamiento del sistema de control

En este documento encontrarás la explicación del funcionamiento del sistema principal que controla el circuito.

## Diagrama de funcionamiento

Aquí tienes una idea más general de cómo funciona el circuito en forma de diagrama:

<img src="/images/systemDiagram.svg" width="600">

Como puedes ver hay un proceso de escucha en bucle que toma los valores de los que nos proveen los sensores integrados en el circuito (BME280 y SCT-013). Ese bucle de escucha a su vez actúa de emisor para los actuadores (ventiladores) y elementos de monitorización (panel OLED) de nuestro circuito.

Como la información se extrae y se '*inyecta*' en los demás elementos, no se guarda ninguna referencia adicional en memoria a estos datos. Esto hace que el sistema sea más eficiente en recursos.
También, al condensar el proceso en un sólo sistema periódico estamos gastando menos recursos al condensarlos en un sólo proceso paralelo.




