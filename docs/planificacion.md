# Planificación del proyecto
## Breve descripción del producto final

Servicio web que automatiza controles de los empleados y produce estadísticos útiles a la direccíon.

## Usuarios
### Tipos
- Empleado, son los que resuelven los proyectos. En mi caso serán evaluadores, consultores y programadores.
- Dirección, se encarga de organizar a los empleados en diferentes proyectos y a planificar proyectos futuros.

### Historias de usuario
#### Empleado.
> Edu. 23 años. Programador.

- Quiere que el programa reduzca la interacción con el horario.
- Quiere que el programa "genere un horario" y modificarlo en caso de que no esté conforme.
- No quiere introducir vacaciones, ni días no laborales.
- Necesita poder validar el horario antes de ser entregado.
- Quieren indicar cuantas horas han dedicado en cada proyecto.

#### Directivo.
> Luis. 40 años.

- Quiere saber cuantas horas totales se han realizado en el proyecto X.
- Quiere conocer cuanto está costando llevar a cabo el proyecto X.
- Quiere saber cómo de eficientes están siendo sus empleados.
- Quiere mejorar sus planificaciones, apoyándose en la opinión de sus empleados y en la eficiencia en el proyecto X una vez se ha finalizado.

## Milestones
Cada uno de los checkpoints por los que el desarrollo tendrá que pasar y algunas aclaraciones.

#### [0.1](https://github.com/morevi/jobcontrol/milestone/1)
> Control horario - Presets, descarga, edición, confirmación y almacenamiento

Manejo básico de los controles de horarios. 
- En el servicio se podrán almacenar los presets, tanto el común, como el individual a cada usuario.
- Se tendrá que poder modificar, de forma completa o parcial, el horario que tiene que entregar.
- Una vez confirmado/enviados los cambios se procederá al almacenamiento.

No se tendrán en cuenta aún la bolsa de horas ni los festivos.

Este hito permite a los empleados empezar a usar el servicio y reducir un poco la interacción con el control horario.

#### [0.2](https://github.com/morevi/jobcontrol/milestone/2)
> Control horario - Bolsa de horas, vacaciones y no laborales automáticos.

- Las vacaciones se generan conforme avanza el año. Con un máximo de X días.
- Los días no laborales se obtendrán desde la web.
- Se almacenará la bolsa de horas del empleado, donde se incrementará o disminuirá el valor de horas disponibles según el horario entregado por el empleado.

Permite automatizar la toma de vacaciones y de días festivos, además del uso del horario flexible. Se finaliza el desarrollo de la correspondiente al control horario.

#### [0.3](https://github.com/morevi/jobcontrol/milestone/3)
> Control proyectos - Almacenamiento de horas, valoración de la planificación y obtención de estadísticas.

- El empleado podrá almacenar las horas en cada proyecto durante esa semana.
- El directivo podrá podrá obtener las horas en cada proyecto.
- El directivo podrá ver el coste actual del proyecto.
- El directivo podrá almacenar una planificación para un proyecto.
- El directivo podrá comparar la planificación con las horas realmente trabajadas en el proyecto.
- El empleado podrá indicar el índice de satisfacción sobre esa planificación.

Este hito permite a los empleados reducir la interacción con el control de proyectos y, al directivo, obtener ciertos estadísticos. Finaliza la parte correspondiente al control de esfuerzos.
