# Task runner
### Requisitos
- fácil de usar
- sintaxis sencilla
- frecuente actividad de mantenimiento del proyecto
- pocas dependencias

### Comparación
Se han comparado: poethepoet, invoke, taskipy, doit, make.

Primero se descartó make, este añade dependencias externas a python, cosa que puede ser evitada haciendo uso de un paquete de python que se encargue de hacer de task runner.

Los demás quedan divididos en 2 grupos: configuración en python o en TOML.

Taskipy y poethepoet ambos son muy similares en sintaxis y en funcionalidad, con su configuración dentro del pyproject.toml, evitando añadir otro fichero al proyecto. Ambos son proyectos con similar actividad en el repositorio.

Doit se descarta, ya que en comparación a invoke, su configuración es bastante más compleja.

Invoke, por otro lado, es sencillo de configurar. Valoro positivamente que se añada un nuevo fichero tasks.py al root del proyecto, ya que favorece la separación, por un lado dependencias y por otro las automatizaciones del proyecto. Además, invoke es bastante popular en comparación a los anteriores (obviando make), lo que hará mucho más sencillo obtener soporte en caso de tener problemas con la herramienta. 

Por ello se ha escogido Invoke como nuestro task runner.
