# Planificación del proyecto
## Breve descripción del producto final

Servicio web que automatiza controles de los empleados y produce estadísticos útiles a la dirección.

## Usuarios
- Empleado, son los que resuelven los proyectos. En mi caso serán evaluadores, consultores y programadores.
- Dirección, se encarga de organizar a los empleados en diferentes proyectos y a planificar proyectos futuros.

## User journey
- El empleado no quiere tener que entregar los documentos, son repetitivos y toman algo de tiempo. Dado que es obligatorio entregar este horario. Podrán entregar al microservicio el horario y las horas de cada proyecto, realizando el mínimo de interacción que sea posible y reduciendo el tiempo de realización de esta tarea. Queremos hacer la entrega del horario de semanalmente, para poder fusionarla con la entrega del cargo de horas a proyectos.

- Al directivo le gustaría que, al crear los proyectos se le recomendase qué empleados son los más aptos, según las habilidades necesarias para llevarlo a cabo. Así puede asignar a empleados que alcanzan el nivel necesario y reservar a empleados de alto nivel para las tareas más difíciles.

## [Historias de usuario](https://github.com/morevi/jobcontrol/issues?q=is%3Aopen+is%3Aissue+label%3Auser-stories)
- HU1 Como empleado, quiero reducir el tiempo en el que realizo la tarea de entregar el _horario_ y las horas en cada proyecto.
- HU2 Como directivo, cuando cree un proyecto quiero recibir una recomendación de empleados, según las habilidades necesarias del proyecto y los empleados, para mejorar la planificación general de la empresa.

## Roadmap/milestones

### [M0](https://github.com/morevi/jobcontrol/milestone/1) Clases _Horario_ y _Proyecto_.
Estructuras de datos sobre la que almacenar los datos relativos a los horarios y a los proyectos.
- _Horario_. Contiene el horario que un usuario ha seguido durante la semana, así como el seguimiento de sus horas adelantadas atrasadas y vacaciones.
- _Proyecto_. Contiene la planificación, las _skills_ necesarias, los empleados asignados y horas realizadas por cada empleado.

Este _milestone_ es _interno._

### [M1](https://github.com/morevi/jobcontrol/milestone/2) Métodos de clases _Horario_ y _Proyecto_.
Métodos de clase que permitan _set_ y _get_ de datos en las estructuras _Horario_ y _Proyecto_.
También métodos que permitan extraer datos elaborados:
- relación Tiempo real/Tiempo planificación,
- cálculo de horas adelantadas y atrasadas.

Este _milestone_ es _interno._

### [M3](https://github.com/morevi/jobcontrol/milestone/3) Controladores para las clases _Horario_ y _Proyecto_.
Clases que se encarguen de manejar la lógica del manejo de peticiones que trabajan sobre _Horarios_ y _Proyectos_.
Estos controladores deben:
- Cada método debe válidar las entradas,
- debe construir una salida _json_, con la estructura establecida.

Este _milestone_ es _interno._

### [M4](https://github.com/morevi/jobcontrol/milestone/3) Microservicio.
Microservicio que permite la interacción con los horarios y proyectos.
Debe:
- incluir los _endpoints_ necesarios para poder realizar las peticiones 
- ser capaz de ser desplegado en la nube

_Externo_
