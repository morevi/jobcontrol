# Integración continua

## Requisitos

- Buen tier gratuito
- Matriz de versiones
- Hosteado en internet
- Poder utilizar docker

## Búsqueda

Existen muchísimos sistemas de CI, puedes echar un vistazo a [ligurio/awesome-ci](https://github.com/ligurio/awesome-ci) para ver una tabla con muchos de ellos y algunas de sus características.

## Análisis

El requisito de que deba estar hosteado en internet, y no self-hosted, se debe a que así podremos abstraer la capa de administración y configuración del servidor y dejar todo eso al servicio en internet. En el pasado he tratado de utilizar DroneCI y WoodpeckerCI (un fork).

Hacer uso de una matriz en la configuración de un servicio de CI nos permitirá probar nuestro código con varias versiones del lenguaje. Algunos servicios que permiten el uso de esta funcionalidad son CircleCI, Actions y TravisCI, por nombrar algunos de los más conocidos y con gran cantidad de información disponible en Internet.

El tier gratuito de TravisCI, ofrece un limitado número de créditos no recargables, lo que es un factor muy restrictivo a largo plazo. Github Actions y CircleCI ambos ofrecen planes gratuitos basados en minutos mensuales, es decir, recargables. Esto nos podría permitir organizar nuestras ejecuciones para aprovechar los minutos sin quedarnos colgados en ningún momento, y en caso de consumirlos, al acabar recuperaríamos los minutos.

Sobre ambos (Actions y CircleCI) podremos lanzar nuestra imagen para ejecutar los tests, pero como CircleCI ofrece más minutos, será este servicio el que utilicemos para realizar la ejecución sobre las diferentes versiones del lenguaje, y Actions para ejecutar el test con docker.

# Versiones de python a probar

Nuestra aplicación, se basa en python3.8, la última versión fuera de "bugfixes" ([info](https://devguide.python.org/#status-of-python-branches)). es decir cada actualización que recibe se tratará de "security updates", lo que hace que la consideremos más estable que las siguientes versiones.

A partir de la 3.8, tendremos que probar además las futuras versiones, 3.9 y 3.10, para poder predecir cambios importantes que requieran intervención de los desarrolladores. Es vital mantenerse actualizado y estar al día con las "security updates".

Otra razón para enfocarnos en versiones futuras es que las versiones pasadas quedan pronto obsoletas (p.e. python 3.6 no recibirá más actualizaciones a partir del 23 de Diciembre, [info](https://endoflife.date/python)), según el modelo de desarrollo de python (una nueva versión recibe mantenimiento durante 5 años). Esto hace que sea importante ir actualizando nuestra aplicación, pero con cierto cuidado, dejando primero que actualicen primero los proyectos de nuestras dependencias. Probar nuevas versiones permite asegurar que pasen los test a futuro.
