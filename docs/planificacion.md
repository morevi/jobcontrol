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
Una vez se han generado las `user-stories` a partir de las `épicas`, y dispuestas de forma ordenada y agrupada por el valor que ofrece al usuario, se puede tratar de agrupar estas para formar los _milestones_. Puede ver la disposición de las `user-stories` en el proyecto de github [`story-map`](https://github.com/morevi/jobcontrol/projects/1). Usar esta herramienta permite expandir las `epicas` en HUs de forma más rápida y convertir a _issues_ asociados a _milestones_ de forma rápida.

Con el objetivo de que todos los milestones sean MVP con valor, se ha seguido una estrategia división vertical del programa: cada _milestone_ (excepto M0) tratará de añadir funcionalidad, de manera que cada entrega proporcione cierto valor a los usuarios. Es decir, desde M1 se tratará de entregar un fragmento del microservicio total, que en cada iteración aporte mayor valor y funcionalidad.

Todos los _milestone_ a partir del M0 deberían de ser tangibles y útiles desde la perspectiva del usuario. Además trataran de incluir un mínimo de funcionalidad que proporcione un valor completo, (ha de ser utilizable por alguno de los usuarios), y además tengan sentido que vayan juntas en el mismo _milestone_ (veáse M4, funcionalidad independiente pero ofrecen el mismo valor).

Como anotación, señalar que en cada _milestone_ que aparece en este documento, se han indicado unas HUs de forma orientativa: para completar el milestone es probable que esas Hus se hayan marcado como terminadas, o al menos, se hayan realizado tareas relacionadas a esas HUs. En la práctica, solo al M0 se le han asignado HUs ya que es por donde empezaremos a crear tareas y a programar, las HUs se irán asignando y moviendo de _milestone_ conforme avanza el desarrollo.

### [M0](https://github.com/morevi/jobcontrol/milestone/1) Clases _Horario_ y _Proyecto_.
Estructuras de datos sobre la que almacenar los datos relativos a los horarios y a los proyectos.
- _Horario_. Contiene el horario que un usuario ha seguido durante la semana, así como el seguimiento de sus horas adelantadas atrasadas y vacaciones.
- _Proyecto_. Contiene la planificación, las _skills_ necesarias, los empleados asignados y horas realizadas por cada empleado.

Este _milestone_ es _interno._

### [M1](https://github.com/morevi/jobcontrol/milestone/2) Servicio básico de horarios.
Microservicio básico que nos permita subir y entregar horarios. Reduce el tiempo de entrega de los horarios.

### [M2](https://github.com/morevi/jobcontrol/milestone/3) Servicio básico de Proyectos.
Microservicio básico que permita crear proyectos y su planificación, y anotar horas en cada proyecto.
Los directivos podrán comenzar a repartir los proyectos y los empleados trabajar en ellos.

### [M3](https://github.com/morevi/jobcontrol/milestone/4) Información sobre el horario.
Ampliación de la funcionalidad del microservicio de horarios, que:
- permita visualizar los días de vacaciones,
- permita visualizar las horas adelantadas/atrasadas,
- permita visualizar los días festivos,
- deje modificar el horario.

Permite a los empleados distribuir de forma efectiva sus vacaciones y aprovechar el horario flexible. Los horarios generados ahora deberán indicar los días festivos.

### [M4](https://github.com/morevi/jobcontrol/milestone/5) Estadísticas de los proyectos.
Ampliación de la funcionalidad del microservicio de proyectos, que incluirá:
- función para el calculo de coste del proyecto,
- función para la obtención de la eficiencia de los trabajadores,
- valoración del plan de proyecto.
- obtener recomendacion de empleados basado en las habilidades asignadas al proyecto

Permite al directivo obtener información útil para la dirección de la empresa y mejorar las futuras planificaciones de proyectos.
