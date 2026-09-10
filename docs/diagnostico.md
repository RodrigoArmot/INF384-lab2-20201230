Defectos encontrados:
1. El push colocado en el pipeline como desencadenante para realizar el job, puede provocar que en un repositorio grande,
   con múltiples ramas activas, el proceso de validación y empaquetamiento pueda aumentar mucho y retrasar el envió a
   producción.
2. En el apartado de fetch-depth = 0 cubre todo el repositorio completo, lo puede provocar lentitud en el proceso, debido
   a la descarga de toda la repo y no solo de la rama principal que se va a usar.
3. Varias veces se descarga entre los dos jobs el los mismos paquetes de Python y código, lo que genera lentitud
   innecesaria cuando podrían compartir los mismos recursos mediante una cache.
4. Se tienen que fijar las verciones en las dependencias, en especial en el sistema operativo, ya que se indica
   ubuntu-latest, lo cual podría ser riesgoso si la nueva versión del sistema operativo tiene incompatibilidades. 
