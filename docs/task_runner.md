# Task runner
### Requisitos
- que permita establecer rutinas ejecutables desde una misma instrucción,
- frecuente actividad de mantenimiento del proyecto, sobre todo el tiempo de respuesta desde la creación de un issue y el tiempo entre commits.
- pocas dependencias,
- específico al lenguaje de programación usado,
- configuración en un fichero aparte, para favorecer la modularidad.

### Encontrado
Buscando por _python task runner_ y _python task manager_ en google, se han encontrado las siguientes alternativas: poethepoet, invoke, taskipy, doit, make. Todos los encontrados cumplen el primer requisito.

### Make
- Aunque tiene ya 45 años, su último commit fue este pasado Noviembre. Recibe issues constantemente que no parecen recibir respuesta. ✗
- Incluye varias dependencias externas a python. ✗
- Creado para C/C++, pero útil en cualquier ámbito. ✗
- Configuración en un Makefile. ✓

### Poethepoet
- Es un proyecto reciente con pocos commits, los issues que recibe parecen ser respondidos rápidamente. ✓
- Incluye algunas dependencias. ✗ 
- Específico de python. ✓
- Configuración en el propio pyproject.toml. ✗

### Taskipy
Curiosamente similar a poethepoet

### Doit
- Parece tener un tiempo de respuesta de pocos días, lo cual es bueno. ✓
- Incluye algunas dependencias. ✗
- Específico de python. ✓
- Configuración en un fichero aparte. ✓

### Invoke
- Parece tardar algo más de una semana en responder a los issues. (Medio punto) 
- No incluye más dependencia que sí mismo. ✓
- Específico de python. ✓
- Configuración en un fichero aparte, tasks.py. ✓

## Decisión
Invoke recibe una puntuación de 3.5/4 con respecto a los criterios que hemos descrito anteriormente.
