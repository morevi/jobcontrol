# JobControl

## El problema
En la empresa en la que trabajo actualmente, es necesario que cada empleado entregue de forma semanal/mensual los siguientes documentos:
- Control de esfuerzos. Semanal. Recoge en un excel cuántas horas ha dedicado a cada uno de los proyectos en los que ha trabajado. Sirve para que los cargos superioes estimen el tiempo por proyecto y puedan ver si han previsto de forma correcta
- Control horario. Mensual. Como la empresa ofrece horario flexible, los empleados deben declarar el horario que han seguido durante el mes (hora de entradas, salida y descansos).

Incluso si se ha repetido el mismo horario durante un tiempo, es necesario modificarlo para anotar que día fué festivo, vacaciones, fechas, etc.

Es una tarea repetitiva y tediosa que todos los empleados preferirían evitar, o al menos, reducir la atención que requiere.

## La idea
Automatizar aunque sea un poco el proceso de generar estos documentos. He incluir funcionalidad que facilite otras tareas que tambien se realizan en la empresa:

### Control de esfuerzos
- Aprovechar el uso de horarios "default" que puedan ser repetidos, y modificados en caso de excepción (p.e. "siempre trabajo de 7 a 15, pero este miercoles no trabajaré, así que haré mis horas el sábado"), para reducir el tiempo de edición del documento.
- Recoger de manera actualizada los días festivos desde la web y aplicarlos sobre los horarios.
- Simplificar el proceso de coger vacaciones y de aprovechar el horario flexible y haciendo uso de una "bolsa" de horas

Es decir, el empleado solo tendrá que realizar las modificaciones oportunas al horario generado, y confirmarlo.

### Control horario
- Completar el documento solo a partir de las horas en cada proyecto realizadas esa semana
- Podría ser de utilidad para la direccion que el programa generase un estadístico de horas totales de varios empleados por proyecto, e incluso calcular el costo total del proyecto

En definitiva, el empleado solo tendra que introducir semanalmente las horas en cada proyecto, y el directivo obtendrá información de utilidad en su trabajo.

## Documentacion
- [Configuracion del repositorio](docs/entorno.md)
