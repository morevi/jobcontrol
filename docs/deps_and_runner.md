# Dependency manager

Se ha comparado poetry y pip. Se elegido poetry, ya que es sencillo de usar, y es capaz de realizar tareas de construcción y publicación de paquetes de python.

# Task runner

Se han comparado: poethepoet, invoke, taskipy, doit, make.

Primero se descartó make, este añade dependencias externas a python, cosa que puede ser evitada haciendo uso de un paquete de python que se encargue de hacer de task runner.

Los demás quedan divididos en 2 grupos: configuración en python y configuracion en TOML.

Taskipy y poethepoet ambos son muy similares en sintaxis y en funcionalidad, con su configuración dentro del pyproject.toml, evitando añadir otro fichero al proyecto. Poethepoet es un poco más popular, pero no por mucho, y ambos proyectos parecen llevar el mismo ritmo de desarrollo y actualizaciones.

Doit se descarta, ya que en comparación a invoke, su configuración es bastante más compleja.

Invoke, por otro lado, es sencillo de configurar. Valoro positivamente que se añada un nuevo fichero tasks.py al root del proyecto, ya que favorece la separación, por un lado dependencias y por otro las automatizaciones del proyecto. Además, invoke es bastante popular en comparación a los anteriores (obviando make), lo que hará mucho más sencillo obtener información y soporte en caso de tener problemas con la herramienta. Por todo ello se ha escogido Invoke como nuestro task runner.


