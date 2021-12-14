# Marco de tests

## Requisitos
- Legibilidad, facilidad visual de interpretar el output de los tests
- Configurable, que ofrezca distintos tipos de output y permita filtrado
- Fixtures, setup y teardown (está bien tener este tipo de funcionalidad, aunque luego decida no usarse).
- Mantenimiento: tiempo de respuesta a issues y tiempo entre commits
- Permite diferentes librerías de aserciones, esto nos permite decidir a nosotros qué aserciones usar, y no vernos obligados a usar las que vengan con el marco.

## Búsqueda
Se ha realizado una búsqueda en _google_ de los términos: "python test framework", "python testing".

## Análisis

### WARD
Es un marco de tests que se centra en la legibilidad por lo que mientras los demás empatan en este aspecto, WARD destaca, ofreciendo un output muy limpio y colorido. Se puede configurar desde el pyproject.toml, o usando argumentos desde el comando (definidos con el task runner). Ofrece _fixtures_ para poder reutilizar la creación de objetos. También permite el uso de _tags_ para filtrar la ejecución de los tests para cuando se está depurando un grupo de funciones concretas. También ofrece _setup_ y _teardown_.
Permite usar diferentes librerías de aserciones.
El proyecto aún no recibe mucha visibilidad, así que la mayoría de issues y respuestas son de colaboradores frecuentes. Aún así, estos no tardan mucho en responder.

### PYTEST
Ofrece _fixtures_.
El proyecto es muy activo, buen tiempo de respuesta y commits frecuentes en el repositorio.
La configuración puede ser realizada mediante opciones del comando con el que se ejecute o en un archivo de configuración con el formato que queramos (_pytest.ini, tox.ini, pyproject.toml, setup.cfg_).
Permite usar diferentes librerías de aserciones.

### NOSE y NOSE2
Similar a pytest. El la documentación, NOSE indica que no está siendo mantenido. Y NOSE2 (que se define como una ampliación de unittest) te enlaza hacia PYTEST. Como parece que son proyectos que no están muy convencidos de sí mismos, no he indagado más en el resto de requisitos, y serán descartados.

### UNITTEST
Además de ser el marco oficial de python, también incluye su propia librería de aserciones. Ofrece _fixtures_, _setup_ y _teardowns_.

## Conclusión
Entre PYTEST y WARD, este último, como he destacado antes, ofrece una salida muy legible. Ofrece muchas otras características similares a las de PYTEST. En cuanto a la configuración, tiene sentido hacerla, o en el pyproject o en el tasks.py, el resto de ficheros que ofrece PYTEST son un bonito extra pero no proporcionan una ventaja real a la hora de realizar la elección.

Se ha elegido WARD.

# Librería de aserciones
## Requisitos
- sintaxis sencilla de entender.
- output de las aserciones junto a WARD, no debe ser demasiado expresivo, no queremos que el contenido sea tenga demasiadas florituras y complique analizar el resultado.
- debe ofrecer comprobaciones preparadas que nos simplifiquen el trabajo más adelante. Por ejemplo, para asegurar que cierto entero es un año.
- Simplicidad de uso

## Búsqueda
Se ha realizado una búsqueda en _google_ de los términos: "python assertion library", "python python assert alternatives".

## Análisis

### Default assert
- No ofrece ninguna sintaxis más allá de usar la directiva `assert`. Sin embargo, realizar nuestras comprobaciones de la misma forma que escribiríamos cualquier otra condición en python permite a esta opción ser la más polivalente.
- Como output muestra solo la diferencia entre lo que se esperaba y lo obtenido de la aserción. Además nos permite usar nuestros propios mensajes AssertionError.
- No ofrece nada. Si quieres algo tendrás que escribir las comprobaciones usando python. Como he dicho, esto la hace la opción más versátil.
- Si sabes python sabes usar esta.

### Assertpy
- La sintaxis busca el lenguaje natural, haciéndola más sencilla de leer pero un poco más pesada de escribir.
- La salida es parecida al de _assert_, pero no nos permite modificar la salida. 
- Es ofrece la mayor cantidad de aserciones especiales.
- No tiene ningún misterio usar Assertpy

### Grappa
- Ofrece una sintaxis un poco más ligera a Assertpy, también buscando el lenguaje natural, y te da a elegir comenzarlas por 'expect' o 'should'
- La salida generada es el más expresivo, además de usar varias líneas para explicar la aserción, te da opción de mostrar el código (cosa que ya logramos con WARD), además del trace.
- Ofrece menos aserciones que Assertpy
- No tiene ningún misterio usar Grappa

### Unittest
Trata de ser tanto un framework como una librería de aserciones. Y fuerza a las aserciones a ser utilizadas bajo una clase de tests, cosa que añade otra capa, que quizás no sea necesaria en el tamaño de nuestra aplicación. Todo esto, en principio ofusca el uso de esta librería.


## Decisión
Una vez analizados se ha optado por Assertpy
