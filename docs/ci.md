# Integración continua

## Requisitos

- Buen tier gratuito
- Matriz de versiones
- Hosteado en internet
- Poder utilizar docker

## Búsqueda

Existen muchisimos sistemas de CI, puedes echar un vistazo a [ligurio/awesome-ci](https://github.com/ligurio/awesome-ci) para ver una tabla con muchos de ellos y algunas de sus características.

## Análisis

El requisito de que deba estar hosteado en internet, y no self-hosted, se debe a que así podremos abstraer la capa de administración y configuración del servicio y dejar todo eso al servicio en internet. En el pasado he tratado de utilizar DroneCI y WoodpeckerCI (un fork).

Hacer uso de una matriz de versiones en la configuración de un servicio de CI nos permitirá probar nuestro código con varias versiones del lenguaje. Algunos servicios que permiten el uso de esta funcionalidad son CircleCI, Actions y TravisCI, por nombrar algunos de los más conocidos y con cantidad de información disponible en Internet.

El tier gratuito de TravisCI, ofrece un número de créditos no recargables, lo que es un factor muy limitante a largo plazo. Github Actions y CircleCI ambos ofrecen planes gratuitos basados en un número de minutos mensuales, lo que nos podría permitir organizar nuestras ejecuciones para aprovechar los minutos sin quedarnos colgados en ningún momento. 

Sobre ambos (Actions y CircleCI) podremos lanzar nuestra imagen para ejecutar los tests, pero como CircleCI ofrece más minutos, será este servicio el que utilicemos para probar sobre las diferentes versiones del lenguaje, y Actions para ejecutar el test con docker.
