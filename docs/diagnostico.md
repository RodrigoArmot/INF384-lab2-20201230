Defectos encontrados:
1. El push colocado en el pipeline como desencadenante para realizar el job, puede provocar que en un repositorio grande,
   con múltiples ramas activas, el proceso de validación y empaquetamiento pueda aumentar mucho y retrasar el envió a
   producción.
2. En el apartado de fetch-depth = 0 cubre todo el repositorio completo, lo puede provocar lentitud en el proceso, debido
   a la descarga de toda la repo y no solo de la rama principal que se va a usar, ademas cuando se publica no muestra el
   versionamiento sino un nombre generico que no permite darle seguimiento.
3. Varias veces se descarga entre los dos jobs el los mismos paquetes de dependencias y código, lo que genera lentitud
   innecesaria cuando podrían compartir los mismos recursos mediante una cache.
4. Se tienen que fijar las verciones en las dependencias, en especial en el sistema operativo, ya que se indica
   ubuntu-latest, lo cual podría ser riesgoso si la nueva versión del sistema operativo tiene incompatibilidades. 


El defecto que explica la duracion:
El que explica mejor el mayor consumo de tiempo es el defecto 3, ya que el pipeline gasta mucho tiempo descargando de nuevo el código y las dependencias, de hecho se ve como en ambos jobs se hacen las mismas tareas que ahorrarían espacio.

El vinculo con el caso 3:
El problema que ataca principalmente al caso de la sesion 1 es el defecto 1 ya que el disparador es con cada push, lo que provoca que la la historia se devuelva a la etapa anterior y tenga que pasar por revision humana, ya que como indica el caso 76 de 94 son devueltos a una etapa anterior.

Metrica DORA beneficiada:
Se espera mejorar el tiempo de entrega del cambio, ya que con las intervenciones a realizar, se puede tener una reducción significativa del tiempo total de los jobs.

Numero concreto:
Se va a utilizar el Usage para poder realizar la comparación de los tiempos.

Se declaró la versión 1.3.5. Desde el tag `v1.2.0` (commit `b7e44ce`), el historial contiene los siguientes cambios sobre el código del paquete:

- `b481aa6 fix(tarifas): redondear el costo por peso a dos decimales`
- `6ba3804 fix(validaciones): colapsar espacios repetidos en el nombre del cliente`
- `562e631 feat(tarifas): agregar desglose de la tarifa calculada`
- Incluyendo los 2 fix del laboratorio pasado.

Actualemente no se puede resolver versiones de forma automaizada. 
