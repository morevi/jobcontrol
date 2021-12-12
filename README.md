# JobControl

## El problema
En la empresa en la que trabajo actualmente, es necesario que cada empleado entregue de forma semanal/mensual los siguientes documentos:
- Control de esfuerzos. Semanal. Recoge en un EXCEL cuántas horas ha dedicado a cada uno de los proyectos en los que ha trabajado. Sirve para que los cargos superiores estimen el tiempo por proyecto y puedan ver si han previsto de forma correcta.
- Control horario. Mensual. Como la empresa ofrece horario flexible, los empleados deben declarar el horario que han seguido durante el mes (hora de entradas, salida y descansos).

Incluso si se ha repetido el mismo horario durante un tiempo, es necesario modificarlo para anotar que día fue festivo, vacaciones, fechas, etc.

Es una tarea repetitiva y tediosa que todos los empleados preferirían evitar, o al menos, reducir la atención que requiere.

## La idea
Automatizar aunque sea un poco el proceso de generar estos documentos e incluir funcionalidad que facilite otras tareas que se realizan en la empresa:

### Control horario
- Aprovechar el uso de horarios "default" que puedan ser repetidos, y modificados en caso de excepción (p.e. "siempre trabajo de 7 a 15, pero este miércoles no trabajaré, así que haré mis horas el sábado"), para reducir el tiempo de edición del documento.
- Recoger de manera actualizada los días festivos desde la web y aplicarlos sobre los horarios. Por tema de planificación, los días festivos ya están apuntados, junto a las vacaciones y la previsión de tiempos de cada proyecto. Sin embargo, hay veces que los ayuntamientos deciden moverlos (2022, 2 de enero desplazado al 26 de mayo). Obtener un calendario de días no laborales actualizado desde la web puede ser útil.
- Simplificar el proceso de coger vacaciones y de aprovechar el horario flexible y haciendo uso de una "bolsa" de horas.

Es decir, el empleado solo tendrá que realizar las modificaciones oportunas al horario generado, y confirmarlo.

### Control de esfuerzos/proyectos
- Completar el documento solo a partir de las horas en cada proyecto realizadas esa semana.
- Podría ser de utilidad para la dirección que el programa generase un estadístico de horas totales de varios empleados por proyecto. Además, añadiendo un coste a la hora (o calculándolo a partir del sueldo de los empleados), calcular el costo total de uno o varios proyectos.
- El directivo trata de prever el tiempo que se tendrá que echar en cada proyecto, al acabar los proyectos podrá obtener la eficiencia del empleado y decidir en las revisiones de sueldos si merece o no una subida. El empleado podrá dar realimentación valorando esa planificación, y el directivo sabrá que debe mejorarlas en futuros proyectos.

En definitiva, el empleado solo tendrá que introducir semanalmente las horas en cada proyecto, y el directivo obtendrá información de utilidad en su trabajo.

## Uso del _task runner_
Tendrás que instalar Invoke con el gestor de dependencias que uses, se recomienda usar Poetry, ya que hace uso de pyproject.toml donde se define Invoke como dependencia del entorno de desarrollo. 

Para ver qué rutinas hemos preparado con el _task runner_:
```shell
inv --list
```
Para comprobar la sintaxis del fichero:
```shell
inv check
```

Para ejecutar los tests:
```shell
inv test
```

## Documentación
- [Configuración del repositorio](docs/entorno.md)
- [Planificación del proyecto](docs/planificacion.md)
- [Gestor de dependencias y tareas](docs/deps_and_runner.md)
