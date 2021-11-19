# Planificación del proyecto
## Breve descripción del producto final

Servicio web que automatiza controles de los empleados y produce estadísticos útiles a la direccíon.

## Usuarios
- Empleado, son los que resuelven los proyectos. En mi caso serán evaluadores, consultores y programadores.
- Dirección, se encarga de organizar a los empleados en diferentes proyectos y a planificar proyectos futuros.

## Historias de usuario

- [HU1]() Como empleado, quiero que cada semana el sistema genere mi horario, a partir del horario base introducido anteriormente, y me permita su modificación y confirmación. De forma que pueda reutilizarlo y ahorrar tiempo.
- [HU2]() Como empleado, quiero que el sistema introduzca los días festivos en el horario sin mi intervención para ahorrar tiempo.
- [HU3]() Como empleado, quiero conocer cuantas horas de vacaciones, me quedan disponibles y cuantas he útilizado, siendo estas deducidas por el sistema a partir de los horarios introducidos para aprovechar al máximo el horario flexible.
- [HU4]() Como directivo, quiero poder crear un proyecto, asignando empleados y la planificación, y una vez acabado el proyecto, obtener información y estadísticos, para mejorar futuras planificaciones.
- [HU5]() Como empleado, necesito declarar semanalmente las horas realizadas en un proyecto, poder visualizar la planificación, y valorar cómo de acertada ha sido, para que el directivo pueda mejorar sus previsiones.

## Milestones
Cada uno de los checkpoints por los que el desarrollo tendrá que pasar y algunas aclaraciones.

### [M0 Clases horario y proyecto básicas]()
Estas clases contienen la información y funcionalidad relativa al manejo básico de los horarios y proyectos. Serán la estructura básica sobre la que podremos empezar el proyecto.
- Clase _Horario_
- Clase _Proyecto_

Este milestone es interno.

#### HUs
- HU1
- HU4

### [M1 Ampliación de funcionalidad]()
Módulo o ampliación de la funcionalidad de la clase _horario_ que logra:
- los horarios mostrarán los días festivos de manera actualizada y automática.
- calculo de vacaciones y su aplicación sobre el horario mediante el uso de la _bolsa_

Módulo que se apoya en la clase _proyecto_ para generar:
- calculo de costo del proyecto
- calculo de la eficiencia de los trabajadores

#### HUs
- HU2
- HU3
- HU5

### [M2 API y despliegue]()
Desarrollo de la API del microservicio, debe poderse realizar el despliegue.
- creación del servicio web
- creación de las rutas y e implementacion de la funcionalidad utilizando los módulos y clases anteriores
- despliege
