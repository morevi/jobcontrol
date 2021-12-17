# Imagen base

## Requisitos

- Menor tamaño.
- Menor tiempo de construcción y ejecución de tests
- Simplicidad del Dockerfile

## Búsqueda 

En dockerhub entre, las imágenes oficiales de Docker de Python, y las de sistema operativo: Debian y Alpine. (Teniendo en cuenta los diferentes tags de cada una).

## Análisis

Primero Alpine, que resultó en una imagen de aproximadamente 900mb, ya que necesita de la inclusión de muchas dependencias para instalar los paquetes de python que necesitemos. El tamaño de la imagen la hace imposible de usar en comparación con las siguientes.

Sobre `debian:slim-bullseye`, siendo `bullseye` el nombre que hace referencia a su versión 11, resultó en una imagen menor, de ~500mb, casi la mitad que Alpine. Además, la construcción sin utilizar caché tomó 4m26s y los tests se ejecutaron en 0.2s. En el dockerfile, dado que se trata de una imagen de OS, es necesario instalar también python.

Por último, de las imágenes oficiales de docker, `python3.8-slim`, `python3.9-slim` o `python3.10-slim` tardarán menos en contruir con nuestras dependencias (1m37s), los tests se ejecutarán en 0.2s y la imagen de tests pesará ~190mb. Haciendola la más ligera y rápida de construir. Además, en el dockerfile no hará falta instalar python.

Usar la imagen más ligera y rápida de construir nos permitirá iterar más rápido en el proceso de desarrollo.

Además, como versión de python, se ha decidido escoger la version 3.8, ya que es una de las versiones más recientes, pero que ya ha salido del periodo de _bugfixes_.Supone un porcentaje considerable de los paquetes de PyPI ([info](https://github.com/hugovk/pypi-tools)) No parece buena opción escoger la 3.10, recién salida (diciembre 2021) por las razones descritas en este [artículo](https://pythonspeed.com/articles/switch-python-3.10/).
