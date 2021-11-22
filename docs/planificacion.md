# Planificación del proyecto
## Breve descripción del producto final

Servicio web que automatiza controles de los empleados y produce estadísticos útiles a la dirección.

## Usuarios
- Empleado, son los que resuelven los proyectos. En mi caso serán evaluadores, consultores y programadores.
- Dirección, se encarga de organizar a los empleados en diferentes proyectos y a planificar proyectos futuros.

## User journey
- El empleado debe indicar el horario que ha seguido de forma mensual, para que los superiores confirmen el pago. 
- El directivo debe planificar los futuros proyectos a partir de las horas realizadas por los empleados, para mantener la empresa con buen rumbo.

## Épicas e Historias de usuario
- E1 Como empleado quiero manejar horarios, para que los cargos superiores sepan cuanto deben pagarme.
    - HU1 Como empleado, quiero subir un horario, para poder reutilizarlo semanalmente.
    - HU2 Como empleado, quiero actualizar el horario, para poder mantener el horario preciso.
    - HU3 Como empleado, quiero confirmar un horario, para que los superiores puedan verlo y puedan pagarme.

- E2 Como empleado quiero gestionar mi tiempo libre restante/disponible, para poder distribuirlo a mi gusto.
    - HU4 Como empleado, quiero visualizar las horas de vacaciones disponibles, para asignarlas a mi gusto.
    - HU5 Como empleado, quiero visualizar cuantas horas llevo atrasadas o adelantadas, para disfrutar el horario flexible.
    - HU6 Como empleado, quiero visualizar los días festivos en el horario, para saber cuando no necesito trabajar.

- E3 Como empleado, quiero asignar horas a cada proyecto, para que el directivo sepa como he distribuido la semana.
    - HU7 Como empleado, quiero declarar cuantas horas he dedicado esta semana a cada proyecto, para que el directivo comprenda el avance en cada proyecto.
    - HU8 Como empleado, al acabar el proyecto quiero valorar la planificación asignada, para que el directivo sepa mejorar futuras planificaciones.

- E4 Como directivo, quiero gestionar proyectos y planificaciones, para poder mejorar la visión a futuro.
    - HU9 Como directivo, quiero crear un proyecto, añadiendo una planificación y asignando empleados, para que los empleados puedan empezar a trabajar.
    - HU10 Como directivo, quiero saber cuánto está costando realizar un proyecto, para asignar el presupuesto de forma razonada.
    - HU11 Como directivo, quiero saber cómo de eficiente esta resultando un empleado, para tenerlo en cuenta en la revisión de sueldos.

## Roadmap/milestones
Una vez se han generado las `user-stories` a partir de las `épicas`, y dispuestas de forma ordenada y agrupada por el valor que ofrece al usuario, se puede tratar de agrupar estas para formar los _milestones_. Puede ver la disposición en el proyecto [`story-map`](https://github.com/morevi/jobcontrol/projects/1).

Con el objetivo de que todos los milestones sean MVP con valor, se ha seguido una estrategia división vertical del programa: cada _milestone_ (excepto M0) tratará de añadir funcionalidad, de manera que cada entrega proporcione cierto valor a los usuarios. Es decir, desde M1 se tratará de entregar un fragmento del microservicio total, que en cada iteración aporte mayor valor y funcionalidad.

Todos los _milestone_ a partir del M0 deberían de ser tangibles y útiles desde la perspectiva del usuario. Además trataran de incluir un mínimo de funcionalidad que proporcione un valor completo, (ha de ser utilizable por alguno de los usuarios), y además tengan sentido que vayan juntas en el mismo _milestone_ (veáse M4, funcionalidad independiente pero ofrecen el mismo valor).

Como anotacion, señalar que en cada _milestone_ que aparece en este documento, se han indicado unas HUs de forma orientativa: para completar el milestone es probable que esas Hus se hayan marcado como terminadas, o al menos, se hayan realizado tareas relacionadas a esas HUs. En la práctica, solo al M0 se le han asignado HUs ya que es por donde empezaremos a crear tareas y a programar, las HUs se irán asignando y moviendo de _milestone_ conforme avanza el desarrollo.

### [M0](https://github.com/morevi/jobcontrol/milestone/1) Clases _Horario_ y _Proyecto_.
Estructuras de datos sobre la que almacenar los datos relativos a los horarios y a los proyectos.
- _Horario_. Contiene el horario que un usuario ha seguido durante la semana, así como el seguimiento de sus horas adelantadas atrasadas y vacaciones.
- _Proyecto_. Contiene las horas realizadas por cada empleado, así como la planificación.

Este _milestone_ es _interno._

#### Historias de usuario:
- HU1
- HU3 

### [M1](https://github.com/morevi/jobcontrol/milestone/2) Servicio básico de horarios.
Microservicio básico que nos permita subir y entregar horarios, permitiendo saber a los cargos superiores cuanto deben pagar a los empleados.

#### Historias de usuario:
- HU1
- HU3 

### [M2](https://github.com/morevi/jobcontrol/milestone/3) Servicio básico de Proyectos.
Microservicio básico que permita crear proyectos y su planificación, y anotar horas en cada proyecto.

#### Historias de usuario:
- HU9
- HU8

### [M3](https://github.com/morevi/jobcontrol/milestone/4) Información sobre el horario.
Ampliación de la funcionalidad del microservicio de horarios, que:
- permita visualizar los días de vacaciones,
- permita visualizar las horas adelantadas/atrasadas,
- permita visualizar los días festivos,
- deje modificar el horario.

Permite a los empleados distribuir de forma efectiva sus vacaciones y aprovechar el horario flexible. Los horarios generados ahora deberán indicar los días festivos.

#### Historias de usuario:
- H2
- H4
- H5
- H6

### [M4](https://github.com/morevi/jobcontrol/milestone/5) Estadísticas de los proyectos.
Ampliación de la funcionalidad del microservicio de proyectos, que incluirá:
- función para el calculo de coste del proyecto,
- función para la obtención de la eficiencia de los trabajadores,
- valoración del plan de proyecto.

Permite al directivo obtener información útil para la dirección de la empresa y futuras planificaciones de proyectos.

#### Historias de usuario:
- HU8
- HU10
- HU11
