# Imagen base

## Requisitos

- Menor tamaño,
- Acceso a mayor cantidad de paquetes,
- Última version de python y de SO lts disponible.

## Búsqueda 

En dockerhub entre, las imágenes oficiales de Docker de Python, y las de sistema operativo: Debian, Ubuntu y Alpine. (Teniendo en cuenta los diferentes tags de cada una).

## Análisis

En cuanto al tamaño, Alpine parece ganar en este aspecto, pero las versiones `slim` o `minimal` de cualquier otra imagen tampoco quedan muy lejos.

Sin embargo las imagenes basadas en Debian o Ubuntu son las que tienen acceso a la mayor cantidad de paquetes.Esto incluye las imágenes oficiales de Docker con el tag _bullseye_, _buster_, etc, pues estas tienen acceso a esos mismos repositorios. Alpine, al utilizar repositorios diferentes y de menor tamaño, podría causar en un futuro que no encontremos algun paquete que necesitemos.

Tanto las imagenes `Python3.10-bullseye` (_bullseye_ es debian) como `debian:bookworm` (aún en testing, no la usaremos), alcanzan la version 3.10.1 de python. Sin embargo Debian como Ubuntu, en sus versiones estables, se quedan en python 3.9.x.

`python3.10-bullseye` cumple los requisitos de versiones y de acceso a paquetes. Pero `python3.10-slim-bullseye`, también cumple el requisito de reducir el tamaño.

