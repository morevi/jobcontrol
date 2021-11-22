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
- E1 Como empleado puedo manejar horarios, para que los cargos superiores sepan cuanto deben pagarme.
    - HU1 Como empleado, quiero subir un horario, para poder reutilizarlo semanalmente.
    - HU2 Como empleado, quiero actualizar el horario, para poder mantener el horario preciso.
    - HU3 Como empleado, quiero confirmar un horario, para que los superiores puedan verlo y puedan pagarme.

- E2 Como empleado puedo gestionar mi tiempo libre restante/disponible, para poder distribuirlo a mi gusto.
    - HU4 Como empleado, quiero visualizar las horas de vacaciones disponibles, para asignarlas a mi gusto.
    - HU5 Como empleado, quiero visualizar cuantas horas llevo atrasadas o adelantadas, para disfrutar el horario flexible.
    - HU6 Como empleado, quiero visualizar los días festivos en el horario, para saber cuando no necesito trabajar.

- E3 Como empleado, puedo asignar horas a cada proyecto, para que el directivo sepa como he distribuido la semana.
    - HU7 Como empleado, puedo declarar cuantas horas he dedicado esta semana a cada proyecto, para que el directivo comprenda el avance en cada proyecto.
    - HU8 Como empleado, al acabar el proyecto puedo valorar la planificación asignada, para que el directivo sepa mejorar futuras planificaciones.

- E4 Como directivo, puedo gestionar proyectos y planificaciones, para poder mejorar la visión a futuro.
    - HU9 Como directivo, puedo crear un proyecto, añadiendo una planificación y asignando empleados, para que los empleados puedan empezar a trabajar.
    - HU10 Como directivo, quiero saber cuánto está costando realizar un proyecto, para asignar el presupuesto de forma razonada.
    - HU11 Como directivo, quiero saber cómo de eficiente esta resultando un empleado, para tenerlo en cuenta en la revisión de sueldos.

## Roadmap/milestones
Siguiendo una estrategia división vertical del programa final, cada _milestone_ (excepto M0) tratará de añadir funcionalidad, de manera que cada entrega proporcione cierto valor a los usuarios.
Todas los _milestone_ a partir del M0 deberían de ser tangibles y útiles desde la perspectiva del usuario. Además trataran de incluir un minimo de funcionalidad que proporcionen un valor completo, y que además tengan sentido que vayan juntas en el mismo _milestone_ (veáse M4, funcionalidad independiente pero ofrecen el mismo valor).

### [M0]() Clases _Horario_ y _Proyecto_.
Estructuras de datos sobre la que almacenar los datos relativos a los horarios y a los proyectos.
- _Horario_. Contiene el horario que un usuario ha seguido durante la semana, así como el seguimiento de sus horas adelantadas atrasadas y vacaciones.
- _Proyecto_. Contiene las horas realizadas por cada empleado, así como la planificación.

Este _milestone_ es _interno._

### [M1]() Servicio básico de horarios.
Microservicio básico que nos permita subir y entregar horarios, permitiendo saber a los cargos superiores cuanto deben pagar a los empleados.

#### Historias de usuario:
- HU1
- HU3 

### [M2]() Servicio básico de Proyectos.
Microservicio básico que permita crear proyectos y su planificación, y anotar horas en cada proyecto.

#### Historias de usuario:
- HU9
- HU8

### [M3]() Información sobre el horario.
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

### [M4]() Estadísticas de los proyectos.
Ampliación de la funcionalidad del microservicio de proyectos, que incluirá:
- función para el calculo de coste del proyecto,
- función para la obtención de la eficiencia de los trabajadores,
- valoración del plan de proyecto.

Permite al directivo obtener información útil para la dirección de la empresa y futuras planificaciones de proyectos.

#### Historias de usuario:
- HU8
- HU10
- HU11


